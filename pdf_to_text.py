import fitz  # PyMuPDF

def pdf_to_text(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    text = ""

    # Loop through each page and extract text
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    return text

# Example usage
pdf_path = "Sample.pdf"
text = pdf_to_text(pdf_path)
print(text)  # Print extracted text
