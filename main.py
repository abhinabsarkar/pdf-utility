import argparse

from pdf_merge import merge_pdfs
from pdf_split import split_pdf


def build_parser() -> argparse.ArgumentParser:
	"""Create and configure command-line arguments for PDF utility commands."""
	parser = argparse.ArgumentParser(description="PDF utility: merge or split PDFs")
	subparsers = parser.add_subparsers(dest="command", required=True)

	merge_parser = subparsers.add_parser("merge", help="Merge multiple PDFs into one")
	merge_parser.add_argument(
		"-o",
		"--output",
		required=True,
		dest="output_file",
		help="Output merged PDF path",
	)
	merge_parser.add_argument(
		"input_files",
		nargs="+",
		help="Input PDF paths in merge order (supports any count)",
	)

	split_parser = subparsers.add_parser("split", help="Split one PDF into pages")
	split_parser.add_argument("input_file", help="Input PDF path")
	split_parser.add_argument("output_folder", help="Output folder for split pages")

	return parser


def main() -> None:
	"""Run PDF utility commands from the command line."""
	parser = build_parser()
	args = parser.parse_args()

	if args.command == "merge":
		merge_pdfs(args.input_files, args.output_file)
	elif args.command == "split":
		split_pdf(args.input_file, args.output_folder)


if __name__ == "__main__":
	main()
