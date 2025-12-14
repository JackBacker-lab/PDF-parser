# PDF-parser

PDF Bible text parser with colored text extraction using PyMuPDF.
This project parses PDF files of the Bible and extracts text with color information according to different parsing modes.

## Requirements
- Python 3.10+
- PyMuPDF

## Installation
```
git clone https://github.com/JackBacker-lab/PDF-parser
cd PDF-parser
pip install -r requirements.txt
```

## Input data
### Expected input directory structure
```text
pdf_files/
├── OT/
│   ├── gen1.pdf
│   └── ...
└── NT/
    ├── mat1.pdf
    └── ...
```

## Usage examples
```bash
python pdf_parser/cli.py --testament OT --mode ches --output output.txt
python pdf_parser/cli.py --testament NT --mode clis --output output_nt.txt
```

## CLI arguments
* --testament: OT or NT
* --mode:
  * ches — Concordant Hebrew English Sublinear
  * clis — Concordant Literal Idiomatic Sublinear
  * cles — Concordant Literal Etymological Sublinear
* --output: output .txt file path

