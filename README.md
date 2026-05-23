# PDF Utility

Simple command-line utility to merge and split PDF files via `main.py`.

## Windows one-click installer (installs prerequisites + builds EXE)

If you want an `.exe` for merge/split and automatic prerequisite setup:

1. Open Command Prompt in the project folder.
2. Run:

```bat
installer\install_and_build.bat
```

What this installer does:

- Installs Python (via `winget`) if not already available.
- Installs Python dependencies from `requirements.txt`.
- Installs `pyinstaller`.
- Builds `pdf-utility.exe` from `main.py`.

Generated output files:

- `installer-output\pdf-utility.exe`
- `installer-output\merge-pdfs.bat`

Quick merge using the generated launcher:

```bat
installer-output\merge-pdfs.bat merged.pdf file1.pdf file2.pdf file3.pdf
```

Direct merge using the generated EXE:

```bat
installer-output\pdf-utility.exe merge -o merged.pdf file1.pdf file2.pdf
```
## Prerequisites

- Python 3.13+ (or any compatible Python 3 version)
- `pypdf` package

Install dependency:

```bash
py -m pip install pypdf
```

If `py` is not available, use your Python executable path instead.

## Usage (via main.py)

All commands are run through `main.py` using subcommands.

General form:

```bash
py main.py <command> [options]
```

## Split a PDF

Split one input PDF into one file per page.

```bash
py main.py split <input_file> <output_folder>
```

Example:

```bash
py main.py split "54911_997942_Hayat_Azfar.pdf" "split_output"
```

Output files are created like:

- `<original_name>_page_1.pdf`
- `<original_name>_page_2.pdf`
- ...

## Merge PDFs

Merge multiple PDFs in the exact order you provide.

```bash
py main.py merge -o <output_file> <input_file_1> <input_file_2> [more_files...]
```

Example:

```bash
py main.py merge -o "merged/output.pdf" \
  "54911_997942_Hayat_Azfar.pdf" \
  "54911_998992_Uba_Chima.pdf" \
  "54911_999061_Khan_Talha.pdf"
```

## Notes

- Use quoted paths if file or folder names contain spaces.
- For merge, output file must be different from all input files.
- Missing input files will raise an error.
