from pathlib import Path

from pypdf import PdfReader, PdfWriter


def split_pdf(input_file: str, output_folder: str) -> None:
	"""Split a PDF into one file per page inside output_folder."""
	input_path = Path(input_file)
	if not input_path.exists():
		raise FileNotFoundError(f"Input PDF not found: {input_path}")

	output_dir = Path(output_folder)
	output_dir.mkdir(parents=True, exist_ok=True)

	reader = PdfReader(str(input_path))
	base_name = input_path.stem

	for page_index, page in enumerate(reader.pages, start=1):
		writer = PdfWriter()
		writer.add_page(page)

		page_output = output_dir / f"{base_name}_page_{page_index}.pdf"
		with page_output.open("wb") as output_stream:
			writer.write(output_stream)
