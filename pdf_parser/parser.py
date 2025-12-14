from pathlib import Path
import fitz

from utils import int_to_rgb, open_pdf

def extract_colored_text(
    page: fitz.Page,
    target_colors: set[tuple[int, int, int]],
    chapter: int
) -> list[str]:
    result = []

    blocks = page.get_text("dict").get("blocks", [])  # type: ignore[attr-defined]
    for block in blocks:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                text = span["text"]
                if text.startswith(":"):
                    if text[1:].strip().isdigit():
                        result.append("\n" + str(chapter) + ":" + text[1:].strip())
                        continue
                
                rgb = int_to_rgb(span["color"])
                if not rgb is None and rgb in target_colors:
                    result.append(text)

    return result


def parse(
    books: dict[str, int], 
    book_names: dict[str, str], 
    dir_path: Path, 
    output_path: Path, 
    target_colors: set[tuple[int, int, int]]
):
    with open(output_path, "w", encoding="utf-8") as f:
        for book, chapters in books.items():
            for chapter in range(1, chapters + 1):
                f.write("\n\n" + book_names[book] + " " + str(chapter))
                doc = open_pdf(dir_path / f"{book}{chapter}.pdf")
                if doc is None:
                    continue

                for page_num in range(len(doc)):
                    page = doc[page_num]
                    text_list = extract_colored_text(page, target_colors, chapter)
                    for text in text_list:
                        f.write(text + " ")

    print(f"Parsed text saved at {output_path}")