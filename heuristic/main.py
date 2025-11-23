"""
Command-line interface for formula detection.
"""

import sys
import json
from pathlib import Path
from formula_detection import FormulaDetector


def main():
    """Main entry point for command-line usage."""
    if len(sys.argv) < 2:
        print("Usage: python main.py <pdf_path> [--verbose]")
        print("Creates:")
        print("  - input/ directory with copied PDF")
        print("  - text_conversions/<pdf_name>/ directory with page1.txt, page2.txt, etc.")
        print("  - results/<pdf_name>_result.json with page numbers and has_formula results")
        print("  --verbose: Print detailed debug information")
        sys.exit(1)

    pdf_path = sys.argv[1]
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    try:
        detector = FormulaDetector()
        results = detector.detect(pdf_path, verbose=verbose)

        # Create results directory and save results to PDF-specific JSON file
        results_dir = Path("results")
        results_dir.mkdir(exist_ok=True)

        pdf_name_without_ext = Path(pdf_path).stem
        results_file = results_dir / f"{pdf_name_without_ext}_result.json"
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        if verbose:
            print(f"\n{'='*80}")
            print(f"Results saved to: {results_file}")
            print(f"{'='*80}")

        # Print summary
        pages_with_formulas = sum(1 for r in results if r["has_formula"])
        summary = f"\n{'='*80}\nSummary: {pages_with_formulas}/{len(results)} pages contain formulas\n{'='*80}"
        if verbose:
            print(summary)
        else:
            print(summary, file=sys.stderr)
            print(f"Results saved to: {results_file}", file=sys.stderr)

    except Exception as e:
        print(f"Error processing PDF: {e}", file=sys.stderr)
        import traceback
        if verbose:
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

