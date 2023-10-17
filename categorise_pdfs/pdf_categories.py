import os
import tabula
import shutil
import fitz  # PyMuPDF

def has_tables(pdf_path):
    try:
        tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True, stream=True)
        return bool(tables)
    except Exception as e:
        print(f"Error checking tables in {pdf_path}: {e}")
        return False

def has_text(pdf_path):
    try:
        with fitz.open(pdf_path) as pdf_document:
            text_exists = any(page.get_text() for page in pdf_document.pages())
        return text_exists
    except Exception as e:
        print(f"Error checking text in {pdf_path}: {e}")
        return False

def has_images(pdf_path):
    try:
        with fitz.open(pdf_path) as pdf_document:
            image_exists = any(page.get_images(full=True) for page in pdf_document.pages())
        return image_exists
    except Exception as e:
        print(f"Error checking images in {pdf_path}: {e}")
        return False

def classify_and_move_pdfs(input_folder, text_output_folder, tables_output_folder, images_output_folder):
    # Create output folders if they don't exist
    os.makedirs(text_output_folder, exist_ok=True)
    os.makedirs(tables_output_folder, exist_ok=True)
    os.makedirs(images_output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)

            if has_tables(pdf_path):
                # Move PDF to tables output folder
                shutil.move(pdf_path, os.path.join(tables_output_folder, filename))
                print(f"Moved '{filename}' to tables output folder.")
            elif has_images(pdf_path):
                # Move PDF to images output folder
                shutil.move(pdf_path, os.path.join(images_output_folder, filename))
                print(f"Moved '{filename}' to images output folder.")
            elif has_text(pdf_path):
                # Move PDF to text output folder
                shutil.move(pdf_path, os.path.join(text_output_folder, filename))
                print(f"Moved '{filename}' to text output folder.")
            else:
                print(f"Unable to determine content type for '{filename}'.")