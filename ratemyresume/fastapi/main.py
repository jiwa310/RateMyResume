import PyPDF2
import fitz
import os 
import base64
import gridfs
import pymongo 
import motor 
import tempfile

from pymongo import MongoClient
from typing import Union, Optional
from uuid import UUID
from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from dotenv import load_dotenv
from io import BytesIO

from comprehend import get_pii_words, edit_pdf

load_dotenv()

mongodb_uri = os.getenv("URI")
database_name = os.getenv("NAME")

app = FastAPI()

class Item(BaseModel):
    id: Optional[UUID] = int
    major_tag: str
    description: str
    likes: int
    pdf_file: bytes  # Add this field to accept bytes for the PDF

    

# Replace with your MongoDB URI and database name
mongodb_uri = mongodb_uri
database_name = database_name

# Create MongoDB client
client = AsyncIOMotorClient(mongodb_uri)

# Access the specified database
db = client[database_name]
db_connection = MongoClient('mongodb://localhost:27017/').myDB

num_pages = None

@app.get("/")
async def read_root():
    print("READING ROOT")
    # Check if a PDF has been uploaded
    if num_pages is not None:
        return {"Number of pages in last uploaded PDF": num_pages}
    else:
        return {"message": "No PDF uploaded yet"}

# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     print("Uploading file...")
#     global num_pages
#     contents = await file.read()
#     byte_reader = PyPDF2.PdfReader(BytesIO(contents))
#     text_reader = PyPDF2.PdfReader(contents)

#     pdf_text = text_reader.pages[0]
#     pdf_bytes = await write_new_pdf(file)  # Await the coroutine here
#     num_pages = len(byte_reader.pages)

#     pii_words = get_pii_words(pdf_text)

#     edit_pdf(path, pii_words)


#     # call post with Item...
#     item = Item(
#         major_tag="HAII",
#         description="BYEEE",
#         likes=137,
#         pdf_file=pdf_bytes  # Store the PDF content in the pdf_file field
#     )

#     # Call the /create-item endpoint to insert the item into MongoDB
#     await create_item(item)

#     return {"filename": file.filename, "num_pages": num_pages}



@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        print("Uploading file...")

        # Create a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        pii_words = get_pii_words(pdf_actual_text)

        # Save the uploaded file to the temporary file
        data = await file.read()
        temp_file.write(data)
        temp_file.close()
        print(temp_file.extract_text())

        # Open the temporary file with PyMuPDF
        edit_pdf(temp_file.name, pii_words)

        # Remove the temporary file when done
        os.unlink(temp_file.name)

        global num_pages
        contents = await temp_file.read()
        byte_reader = PyPDF2.PdfReader(BytesIO(contents))
        text_reader = PyPDF2.PdfReader(contents)

        pdf_text = text_reader.pages[0]
        pdf_actual_text = pdf_text.extract_text()
        pdf_bytes = await write_new_pdf(temp_file)  # Await the coroutine here
        num_pages = len(byte_reader.pages)

        # call post with Item...
        item = Item(
            major_tag="HAII",
              description="BYEEE",
            likes=137,
            pdf_file=pdf_bytes  
        )

        # Call the /create-item endpoint to insert the item into MongoDB
        await create_item(item)

        return {"filename": file.filename}

    except Exception as e:
        return {"error": str(e)}


async def write_new_pdf(file):
    fs = gridfs.GridFS(db_connection)
    print("Retrieving bytes from pdf...")

    # Ensure the file position is at the beginning
    file.file.seek(0)

    # Read the file content and encode it to base64
    encoded_string = base64.b64encode(file.file.read())

    return encoded_string

@app.get("/get-all")
async def get_all_items():
    collection = db["items"]
    items = await collection.find().to_list(length=None)

    # Convert ObjectId to string
    for item in items:
        item["_id"] = str(item["_id"])

    return items

@app.post("/create-item")
async def create_item(item: Item):
    print("Create-item has been called!")
    # Example: Insert item details into MongoDB
    collection = db["items"]  # Replace "items" with your actual collection name
    result = await collection.insert_one(item.dict())

    if result.inserted_id:
        return {"message": "Item created successfully", "item_id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Failed to create item")

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    # Example: Fetch item details from MongoDB based on item_id
    collection = db["items"]  # Replace "items" with your actual collection name
    item = await collection.find_one({"item_id": item_id})
    
    if item:
        return item
    else:
        return {"message": "Item not found"}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    # Example: Update item details in MongoDB based on item_id
    collection = db["items"]  # Replace "items" with your actual collection name
    result = await collection.update_one({"item_id": item_id}, {"$set": item.dict()})
    
    if result.modified_count == 1:
        return {"message": "Item updated successfully"}
    else:
        return {"message": "Item not found"}

# Added PUT endpoint to update items
@app.put("/update-items/{item_id}")
async def update_item_details(item_id: int, updated_item: Item):
    # Example: Update item details in MongoDB based on item_id
    collection = db["items"]  # Replace "items" with your actual collection name
    result = await collection.update_one({"item_id": item_id}, {"$set": updated_item.dict()})
    
    if result.modified_count == 1:
        return {"message": "Item updated successfully"}
    else:
        return {"message": "Item not found"}
    
@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    collection = db["items"]
    result = await collection.delete_one({"_id": ObjectId(item_id)})

    if result.deleted_count == 1:
        return {"message": "Item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"Item with id: {item_id} not found")
    
if client:
    print("Connected to MongoDB")