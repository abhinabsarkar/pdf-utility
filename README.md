# PDF Utility

Simple command-line utility to merge and split PDF files via `main.py`.

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
py main.py split "doc1.pdf" "split_output"
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
  "doc1.pdf" \
  "doc2.pdf" \
  "doc3.pdf"
```

## Notes

- Use quoted paths if file or folder names contain spaces.
- For merge, output file must be different from all input files.
- Missing input files will raise an error.
