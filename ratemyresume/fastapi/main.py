from fastapi import FastAPI, UploadFile, File
import PyPDF2
from io import BytesIO

app = FastAPI()

# Initialize a variable to store the number of pages
num_pages = None

@app.get("/")
async def read_root():
    # Check if a PDF has been uploaded
    if num_pages is not None:
        return {"Number of pages in last uploaded PDF": num_pages}
    else:
        return {"message": "No PDF uploaded yet"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global num_pages
    contents = await file.read()
    reader = PyPDF2.PdfReader(BytesIO(contents))

    # Store the number of pages in the global variable
    num_pages = len(reader.pages)

    return {"filename": file.filename, "num_pages": num_pages}
