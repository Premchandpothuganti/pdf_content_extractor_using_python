from categorise_pdfs.pdf_categories import classify_and_move_pdfs
from pdf_extraction_methods.extractions import extract_images,extract_tables, extract_tables_from_multiple_pdfs,extract_text, extract_text_from_multiple_pdfs

# input_folder = "data"
# text_output_folder = "text_output"
# tables_output_folder = "tables_output"
# images_output_folder = "images_output"

# classify_and_move_pdfs(input_folder, text_output_folder, tables_output_folder, images_output_folder)

# Example usage:
# pdf_path = "text_output/textpdf.pdf"
# text = extract_text(pdf_path)

# pdf_path = "tables_output/data.pdf"
# tables = extract_tables(pdf_path)

# pdf_path = "images_output/imagePDF.pdf"
# extract_images(pdf_path, "output_images")

# using extract_text_from_multiple_pdfs from extract methods
# pdf_folder = "text_output"
# output_folder = "Output_text_files"
# extract_text_from_multiple_pdfs(pdf_folder, output_folder)

#using extract_tables_from_multiple_pdfs from extract methods
# pdf_folder = "tables_output"
# output_folder = "Output_table_files"
# extract_tables_from_multiple_pdfs(pdf_folder,output_folder)
