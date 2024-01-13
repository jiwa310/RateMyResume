from fastapi import FastAPI, UploadFile, File
import PyPDF2
from io import BytesIO

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    reader = PyPDF2.PdfFileReader(BytesIO(contents))

    #USE READER TO DO WHATEVER YOU WANT
    #using reader to get the number of pages in the pdf:
    print(reader.getNumPages())

    return {"filename": file.filename}
