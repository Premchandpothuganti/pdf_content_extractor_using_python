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
            print(text)
            return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

def extract_tables(pdf_path):
    try:
        tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True, stream=True)
        print(tables)
        return tables
    except Exception as e:
        print(f"Error extracting tables from {pdf_path}: {e}")
        return None

def extract_images(pdf_path, output_folder):
    try:
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

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

def extract_text_from_multiple_pdfs(pdf_folder, output_folder):
    try:
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(pdf_folder):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(pdf_folder, filename)
                output_filename = os.path.splitext(filename)[0] + ".txt"
                output_path = os.path.join(output_folder, output_filename)

                # Extract text from the PDF
                text = extract_text(pdf_path)

                if text is not None:
                    # Save the text to a TXT file
                    with open(output_path, "w", encoding="utf-8") as txt_file:
                        txt_file.write(text)
                    print(f"Text extracted from '{filename}' and saved to '{output_filename}'.")
                else:
                    print(f"Error extracting text from '{filename}'.")
    except Exception as e:
        print(f"Error extracting text from multiple PDFs: {e}")

def extract_tables_from_multiple_pdfs(pdf_folder, output_folder):
    try:
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(pdf_folder):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(pdf_folder, filename)

                # Extract tables from the PDF
                tables = extract_tables(pdf_path)

                if tables is not None:
                    # Save each table to a separate CSV file
                    for table_index, table in enumerate(tables):
                        table_filename = f"{os.path.splitext(filename)[0]}_table_{table_index + 1}.csv"
                        table_path = os.path.join(output_folder, table_filename)
                        table.to_csv(table_path, index=False)
                    
                    print(f"Tables extracted from '{filename}' and saved to '{output_folder}'.")
                else:
                    print(f"Error extracting tables from '{filename}'.")
    except Exception as e:
        print(f"Error extracting tables from multiple PDFs: {e}")
