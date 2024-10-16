import logging
import os
from argparse import ArgumentParser
from io import BytesIO

from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


# Constants
ANNOTATION_POSITION_X = 10
ANNOTATION_POSITION_Y = 10


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')


def get_pdf_files(folder_path):
    """
    Retrieve and sort all PDF files in the given folder.

    Parameters:
    folder_path (str): The path to the folder containing PDFs.

    Returns:
    list: Sorted list of PDF file names in the folder.
    """
    try:
        pdf_files = sorted([pdf for pdf in os.listdir(
            folder_path) if pdf.endswith('.pdf')])
        logging.info(f"Found {len(pdf_files)} PDF files in {folder_path}")
        return pdf_files
    except Exception as e:
        logging.error(f"Error reading directory {folder_path}: {e}")
        return []


def add_text_to_pdf(pdf_path, annotation_text):
    """
    Add annotation text and file name to each page of a PDF.

    Parameters:
    pdf_path (str): The path to the PDF file.
    annotation_text (str): The text to annotate the PDF with.

    Returns:
    str: Path to the annotated PDF.
    """
    try:
        # Create a PdfReader object
        existing_pdf = PdfReader(pdf_path)

        # Create a PdfWriter object
        output = PdfWriter()

        # Add text (annotation + file name) to each page of the PDF
        file_name = os.path.basename(pdf_path)
        full_annotation = f"{annotation_text}: {file_name}"

        for i in range(len(existing_pdf.pages)):
            packet = BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            can.drawString(
                ANNOTATION_POSITION_X,
                ANNOTATION_POSITION_Y,
                full_annotation)
            can.save()

            # Move to the beginning of the buffer
            packet.seek(0)

            # Read the new PDF with text
            new_pdf = PdfReader(packet)

            # Merge the text with the existing page
            page = existing_pdf.pages[i]
            page.merge_page(new_pdf.pages[0])
            output.add_page(page)

        # Save the annotated PDF to a temporary file
        output_path = os.path.splitext(pdf_path)[0] + "_temp.pdf"
        with open(output_path, "wb") as outputStream:
            output.write(outputStream)
        return output_path
    except Exception as e:
        logging.error(f"Error processing {pdf_path}: {e}")
        return None


def merge_pdfs(pdf_files, folder_path, output_file):
    """
    Merge annotated PDFs into a single output file.

    Parameters:
    pdf_files (list): List of PDF files to merge.
    folder_path (str): The directory where the PDFs are stored.
    output_file (str): The name of the final merged PDF.

    Returns:
    None
    """
    merger = PdfMerger()
    temp_files = []

    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        pdf_with_text = add_text_to_pdf(pdf_path, "File")
        if pdf_with_text:
            merger.append(pdf_with_text)
            temp_files.append(pdf_with_text)

    output_path = os.path.join(folder_path, output_file)
    with open(output_path, 'wb') as merged_pdf:
        merger.write(merged_pdf)
    merger.close()

    logging.info(f"Combined PDF created at {output_path}")

    # Cleanup temporary files
    for temp_file in temp_files:
        if os.path.exists(temp_file):
            os.remove(temp_file)
            logging.info(f"Deleted temporary file: {temp_file}")


def main():
    """
    Main function that parses arguments and calls the PDF merging function.
    """
    parser = ArgumentParser(description="Merge and annotate PDF files")
    parser.add_argument(
        "folder_path",
        help="Path to the folder containing PDF files")
    parser.add_argument(
        "--output",
        default="merged_output.pdf",
        help="Name of the output merged PDF")
    args = parser.parse_args()

    folder_path = args.folder_path
    output_file = args.output

    # Get list of PDF files
    pdf_files = get_pdf_files(folder_path)
    if not pdf_files:
        logging.error(f"No PDF files found in {folder_path}. Exiting.")
        return

    # Merge PDFs
    merge_pdfs(pdf_files, folder_path, output_file)


if __name__ == "__main__":
    main()