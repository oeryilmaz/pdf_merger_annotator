# PDF Merger and Annotator

## Overview
This Python script merges PDF files, adds file names as annotations to each page, and generates a final merged PDF. I wrote this little function to make it easier for me to compare the event-study plots of different specifications on a mobile device or to print it and work on it when no screen was available. In principle, one can adjust it and simply use it as a PDF merger for any purpose, avoiding online tools etc.

## Features
- Merges multiple PDF files into a single PDF.
- Annotates each page with customizable text (e.g., file name and custom text).
- Cleans up temporary files after processing.

## Requirements
- Python 3.7+
- PyPDF2
- ReportLab

## Installation
1. Clone the repository and install the necessary libraries:
```bash
git clone https://github.com/yourusername/pdf_merger_annotator.git
cd pdf_merger_annotator
```
2. Install the required libraries from the requirements.txt file:
```bash
pip install -r requirements.txt
```

## Using it

1. Place the PDFs you want to merge in a folder on your system.
2. Run the script, providing the folder path containing the PDFs and the output file name:
```bash
python pdf_merger.py "/path/to/your/pdf/folder/" --output combined_output.pdf
```
3. The script will merge all the PDFs in the folder, annotate each page with the file name, and save the merged output as combined_output.pdf (or any other name you provide).

## Example
Take a folder with the PDF files you want to merge
```bash
C:/Users/user0/project0/03_results/02_bunch_of_pdf_files/
```

Run:

```bash
python pdf_merger.py "C:/Users/user0/project0/03_results/02_bunch_of_pdf_files/" --output merged_report.pdf
```

## License
This project is licensed under the MIT License.
