import sys
import fitz  # PyMuPDF
from inference import is_math_xgboost

def classify_pdf_pages(pdf_path: str):
    """
    Classify each page of a PDF as having formula or not.

    Args:
        pdf_path: Path to the PDF file

    Returns:
        List of tuples: (page_number, has_formula, classification)
    """
    doc = fitz.open(pdf_path)
    results = []

    for page_num in range(len(doc)):
        page = doc[page_num]

        # Extract text from the page
        blocks = page.get_text("dict")["blocks"]
        page_text = ""
        all_block_lines = []

        for block in blocks:
            if block["type"] != 0:  # skip images
                continue
            text = ""
            lines = []
            for line in block["lines"]:
                ltext = "".join(span["text"] for span in line["spans"])
                text += ltext + "\n"
                lines.append(line)
            if text.strip():
                page_text += text
                all_block_lines.extend(lines)

        # Classify the page
        if page_text.strip():
            # Use the first few block lines for layout features if available
            block_lines_for_features = all_block_lines[:4] if len(all_block_lines) <= 4 else None
            classification = is_math_xgboost(page_text, block_lines_for_features, page.rect.width)

            # Determine if page has formula
            has_formula = classification in ["displayed", "inline_or_mixed"]

            results.append((page_num + 1, has_formula, classification))
        else:
            # Empty page
            results.append((page_num + 1, False, "prose"))

    doc.close()
    return results

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <pdf_file_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]

    try:
        results = classify_pdf_pages(pdf_path)

        print(f"\nClassification results for: {pdf_path}\n")
        print(f"{'Page':<8} {'Has Formula':<15} {'Classification':<20}")
        print("-" * 45)

        for page_num, has_formula, classification in results:
            formula_status = "Yes" if has_formula else "No"
            print(f"{page_num:<8} {formula_status:<15} {classification:<20}")

        # Summary
        total_pages = len(results)
        pages_with_formula = sum(1 for _, has_formula, _ in results if has_formula)
        print(f"\nSummary: {pages_with_formula}/{total_pages} pages contain formulas")

    except FileNotFoundError:
        print(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

