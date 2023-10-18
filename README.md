# pdf_content_extractor_using_python
extracting the content from PDFs, content includes like Tables, Text, Images

# PDF Content Extractor Using Python

This Python project provides functionality for extracting and categorizing content from PDF files. It includes modules for categorizing PDFs based on their content types, extracting text, tables, and images from PDFs, and saving the extracted content to different output folders.

## Project Structure

```plaintext
pdf_content_extractor_using_python/
│
├── .env
├── categorise_pdfs/
│   ├── __init__.py
│   ├── pdf_categories.py
│
├── pdf_extraction_methods/
│   ├── __init__.py
│   ├── extractions.py
│
├── .gitignore
├── LICENSE
├── main.py
├── README.md
├── output_text/
│   # This folder will contain extracted text from PDFs in TXT format
│
├── output_tables/
│   # This folder will contain extracted tables from PDFs in CSV format
│
├── output_images/
│   # This folder will contain extracted images from PDFs in PNG format
│
├── your_pdf_folder/
│   # This is the folder containing your input PDFs
│   ├── pdf_file1.pdf
│   ├── pdf_file2.pdf
│   └── ...
