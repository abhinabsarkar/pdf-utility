from pathlib import Path
from typing import Iterable

from pypdf import PdfReader, PdfWriter


def merge_pdfs(input_files: Iterable[str], output_file: str) -> None:
	"""Merge PDFs in the exact order provided in input_files."""
	paths = [Path(file_path) for file_path in input_files]
	if not paths:
		raise ValueError("input_files must contain at least one PDF path")

	output_path = Path(output_file).resolve()

	for pdf_path in paths:
		if not pdf_path.exists():
			raise FileNotFoundError(f"Input PDF not found: {pdf_path}")
		if pdf_path.resolve() == output_path:
			raise ValueError("output_file must be different from all input_files")

	writer = PdfWriter()
	for pdf_path in paths:
		reader = PdfReader(str(pdf_path))
		for page in reader.pages:
			writer.add_page(page)

	output_path.parent.mkdir(parents=True, exist_ok=True)
	with output_path.open("wb") as output_stream:
		writer.write(output_stream)
