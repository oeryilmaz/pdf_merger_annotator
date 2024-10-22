# PDF Merger and Annotator

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview
This Python script merges multiple PDF files into a single PDF, adding file names as annotations on each page. It was originally created to make it easier to compare event-study plots across different specifications, but it can be adapted for any use case where PDF merging and annotation are needed, such as avoiding online tools and preserving file privacy.

## Features
- **Merge PDFs**: Combine multiple PDF files into one output PDF.
- **Annotate PDFs**: Add file names or custom text to each page of the PDFs.
- **Temporary File Cleanup**: Automatically cleans up temporary annotated PDF files after merging.

## Requirements
- **Python 3.7+**
- **Dependencies**:
  - [PyPDF2](https://pypdf2.readthedocs.io/) for PDF merging and manipulation.
  - [ReportLab](https://www.reportlab.com/) for adding text annotations to PDFs.
  
  These can be installed via the `requirements.txt` file.

## Installation

1. **Clone the Repository**
   Open your terminal and clone the repository to your local machine:

```bash
git clone https://github.com/oeryilmaz/pdf_merger_annotator.git
cd pdf_merger_annotator
```
2. **Install Dependencies** 
Use pip to install the necessary Python libraries:

```bash
pip install -r requirements.txt
```


## Usage
1. **Prepare Your PDFs**
- Place the PDFs you want to merge into a folder on your system.

2. **Run the Script**
- Open your terminal and navigate to the directory where the script is located.
- Provide the folder path containing the PDFs and specify the output file name:

```bash
python pdf_merger.py "/path/to/your/pdf/folder/" --output combined_output.pdf
```
- The script will merge all the PDFs in the folder, annotate each page with the file name, and save the output as combined_output.pdf (or any name you provide).

### Example

Here’s an example folder structure:

```bash
C:/Users/user0/project0/03_results/02_bunch_of_pdf_files/
```
Run the following command to merge the PDFs in that folder and create a merged PDF file:

```bash
python pdf_merger.py "C:/Users/user0/project0/03_results/02_bunch_of_pdf_files/" --output merged_report.pdf
```

## Troubleshooting
### Common Issues

- No PDFs found in the folder: Ensure the folder path you provided contains valid .pdf files.
- Output PDF not generated: Check that the script has permission to write to the folder where you're trying to save the output.
- Annotations not showing: Verify that ReportLab is installed and working correctly.
- ReportLab Installation on Windows: If you run into issues installing `reportlab` on Windows, download a built distribution of it [here](https://pypi.org/project/reportlab/#files), then install it using:

```bash
pip install path/to/downloaded/reportlab‑x.x.x‑win_amd64.whl
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.