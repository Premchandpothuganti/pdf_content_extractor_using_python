from categorise_pdfs.pdf_categories import classify_and_move_pdfs
from pdf_extraction_methods.extractions import extract_images

input_folder = "data"
text_output_folder = "text_output"
tables_output_folder = "tables_output"
images_output_folder = "images_output"

classify_and_move_pdfs(input_folder, text_output_folder, tables_output_folder, images_output_folder)

# Example usage:
# pdf_path = "path/to/your/pdf/file.pdf"
# text = extract_text(pdf_path)
# tables = extract_tables(pdf_path)
# extract_images(pdf_path, "path/to/output/folder")
