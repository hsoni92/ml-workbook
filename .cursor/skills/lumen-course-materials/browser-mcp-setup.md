# Browser MCP for Lumen

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "browsermcp": {
      "command": "npx",
      "args": ["-y", "@browsermcp/mcp@latest"],
      "env": {
        "PATH": "/home/<user>/.nvm/versions/node/v24.14.0/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
      }
    }
  }
}
```

Adjust the Node version path to match `which npx` after `nvm use`.

1. Install the [Browser MCP](https://browsermcp.io/) Chrome extension.
2. Reload Cursor; enable **browsermcp** under Customize → MCP.
3. Use the Chrome profile where Lumen is logged in; approve the extension when prompted.

Lumen automation uses the **`user-browsermcp`** namespace (`browser` tool), not `cursor-ide-browser`.
