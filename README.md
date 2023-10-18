# PDF Content Extractor Using Python

This Python project provides functionality for extracting and categorizing content from PDF files. It includes modules for categorizing PDFs based on their content types, extracting text, tables, and images from PDFs, and saving the extracted content to different output folders.

## Project Structure

```plaintext
pdf_content_extractor_using_python/
│
├── .env
│
├── your_Data_pdf_folder/
│   # This is the folder containing your input PDFs
│   ├── pdf_file1.pdf
│   ├── pdf_file2.pdf
│   └── ...
|
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
```

## Usage

### Setup
#### Step:1 Clone the repository:
```
https://github.com/Premchandpothuganti/pdf_content_extractor_using_python.git
```
```
cd pdf_content_extractor_using_python
```

#### Step:2 Install dependencies:
```
pip install -r requirements.txt
```
## Running the Code
- To categorize PDFs and move them to different folders based on content types:
```
python main.py
```
## Output
- Extracted text will be saved in the **output_text** folder.
- Extracted tables will be saved in the **output_tables** folder.
- Extracted images will be saved in the **output_images** folder.
