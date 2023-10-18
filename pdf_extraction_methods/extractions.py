import fitz  # PyMuPDF
import tabula
import os

def extract_text(pdf_path):
    try:
        with fitz.open(pdf_path) as pdf_document:
            text = ""
            for page_number in range(pdf_document.page_count):
                page = pdf_document[page_number]
                text += page.get_text()
            return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

def extract_tables(pdf_path):
    try:
        tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True, stream=True)
        return tables
    except Exception as e:
        print(f"Error extracting tables from {pdf_path}: {e}")
        return None

def extract_images(pdf_path, output_folder):
    try:
        with fitz.open(pdf_path) as pdf_document:
            for page_number in range(pdf_document.page_count):
                page = pdf_document[page_number]
                images = page.get_images(full=True)
                for img_index, image in enumerate(images):
                    img = pdf_document.extract_image(image[0])
                    img_bytes = img["image"]
                    image_filename = f"page_{page_number + 1}_img_{img_index + 1}.png"
                    image_path = os.path.join(output_folder, image_filename)
                    with open(image_path, "wb") as img_file:
                        img_file.write(img_bytes)
        print(f"Images extracted to {output_folder}.")
    except Exception as e:
        print(f"Error extracting images from {pdf_path}: {e}")


