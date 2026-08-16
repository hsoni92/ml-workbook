#!/usr/bin/env node
/**
 * Validate every Mermaid block in Markdown files using @probelabs/maid.
 * Maid is a Chevrotain-based Mermaid validator with the same render guarantee
 * as the official Mermaid renderer, but runs in Node without a browser.
 *
 * Usage:
 *   node scripts/validate-mermaid.js [files...]   # explicit files (preferred in pre-commit)
 *   node scripts/validate-mermaid.js              # scan all *.md under bits-pilani/
 *
 * Exit code:
 *   0  all blocks parsed successfully
 *   1  one or more blocks failed to parse
 *   2  unexpected runtime error (missing dep, etc.)
 */

import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import {
  extractMermaidBlocks,
  offsetErrors,
  validate,
  textReport,
} from "@probelabs/maid";

function relPath(absPath) {
  return path.relative(process.cwd(), absPath) || absPath;
}

function discoverTargets() {
  const argv = process.argv.slice(2);
  if (argv.length > 0) {
    return argv.filter((a) => !a.startsWith("-"));
  }
  const notesRoot = path.join(process.cwd(), "bits-pilani");
  const out = [];
  function walk(dir) {
    let entries;
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      return;
    }
    for (const entry of entries) {
      if (entry.name.startsWith(".") || entry.name === "node_modules") continue;
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        walk(full);
      } else if (entry.isFile() && full.endsWith(".md")) {
        out.push(full);
      }
    }
  }
  walk(notesRoot);
  return out;
}

/**
 * Validate a single file. Returns an array of error reports shaped like:
 *   { file, blockIndex, line, report }
 * `line` is the 1-based line number of the opening fence in the markdown file
 * (so the reported column from maid matches when offset is applied).
 */
async function validateFile(absPath) {
  const text = fs.readFileSync(absPath, "utf8");
  // `extractMermaidBlocks` returns blocks in source-offset terms; we re-derive
  // the opening-fence line ourselves because maid's `MermaidBlock` shape
  // varies by version.
  const blockStarts = [];
  const lines = text.split(/\r?\n/);
  for (let i = 0; i < lines.length; i++) {
    if (/^```\s*mermaid\b/i.test(lines[i])) {
      blockStarts.push(i + 1); // 1-based line of the opening fence
    }
  }
  if (blockStarts.length === 0) return [];

  // Maid's block extractor returns objects with `.content` (the inner diagram
  // source, fence stripped). Validate each block in isolation.
  const blocks = extractMermaidBlocks(text);
  if (blocks.length !== blockStarts.length) {
    // Defensive: bail rather than report misleading line numbers.
    throw new Error(
      `Internal: block count mismatch (maid=${blocks.length}, fence-scan=${blockStarts.length}) for ${absPath}`,
    );
  }

  const errors = [];
  for (let i = 0; i < blocks.length; i++) {
    const block = blocks[i];
    const source = block.content;
    if (!source || !source.trim()) continue;

    let result;
    try {
      result = await validate(source);
    } catch (e) {
      errors.push({
        file: absPath,
        blockIndex: i,
        line: blockStarts[i],
        report: `Validator threw: ${e && e.message ? e.message : String(e)}`,
      });
      continue;
    }

    // Maid returns diagnostics with line/column relative to the block source.
    // We translate back to absolute file lines using the opening fence.
    const adjusted = offsetErrors
      ? offsetErrors(result.errors ?? [], blockStarts[i])
      : (result.errors ?? []);

    if (adjusted.length === 0) continue;

    errors.push({
      file: absPath,
      blockIndex: i,
      line: blockStarts[i],
      adjusted,
      source,
    });
  }
  return errors;
}

function formatError(err) {
  const fileLabel = relPath(err.file);
  const report =
    typeof textReport === "function"
      ? textReport(fileLabel, err.source, err.adjusted)
      : JSON.stringify(err.adjusted, null, 2);
  return `  ${fileLabel}:${err.line}\n${String(report)
    .split("\n")
    .map((l) => (l.length > 0 ? `    ${l}` : ""))
    .filter(Boolean)
    .join("\n")}`;
}

async function main() {
  const targets = discoverTargets();
  if (targets.length === 0) {
    console.log("No Markdown files to check.");
    return;
  }

  let totalErrors = 0;
  let filesWithErrors = 0;
  const allErrors = [];

  for (const target of targets) {
    let errors;
    try {
      errors = await validateFile(target);
    } catch (e) {
      console.error(`Unexpected error reading ${relPath(target)}: ${e.message}`);
      process.exitCode = 2;
      return;
    }
    if (errors.length > 0) {
      filesWithErrors += 1;
      totalErrors += errors.length;
      allErrors.push(...errors);
    }
  }

  if (totalErrors === 0) {
    console.log(
      `Mermaid: validated ${targets.length} file(s), no parse errors.`,
    );
    return;
  }

  for (const err of allErrors) {
    console.error(formatError(err));
  }
  console.error(
    `Mermaid: ${totalErrors} block(s) failed to parse across ${filesWithErrors} file(s).`,
  );
  process.exitCode = 1;
}

main().catch((e) => {
  console.error("Validator crashed:", e && e.stack ? e.stack : e);
  process.exit(2);
});
