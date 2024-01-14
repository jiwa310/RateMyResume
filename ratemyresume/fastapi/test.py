import PyPDF2
from io import BytesIO



reader = PyPDF2.PdfReader("example4.pdf")
# contents = file.read()

file_stream = BytesIO(contents)
text_reader = PyPDF2.PdfReader(file_stream) 
pdf_text = text_reader.pages[0].extract_text()
print(pdf_text)