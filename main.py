from categorise_pdfs.pdf_categories import classify_and_move_pdfs


input_folder = "data"
text_output_folder = "text_output"
tables_output_folder = "tables_output"
images_output_folder = "images_output"

classify_and_move_pdfs(input_folder, text_output_folder, tables_output_folder, images_output_folder)
