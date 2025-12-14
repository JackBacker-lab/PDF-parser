from pathlib import Path
import fitz

def int_to_rgb(color: int) -> tuple[int, int, int]:
    if not 0 <= color <= 0xFFFFFF:
        print("color must be 0..0xFFFFFF")
        return None
    return (
        (color >> 16) & 0xFF,
        (color >> 8) & 0xFF,
        color & 0xFF,
    )
    
    
def open_pdf(path: Path) -> fitz.Document | None:
    if not path.exists():
        print(f"[WARN] File not found: {path}")
        return None
    return fitz.open(path)