import PyPDF2
import os 
import base64
import gridfs
import pymongo 
import motor 

from pymongo import MongoClient
from typing import Union, Optional
from uuid import UUID
from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from dotenv import load_dotenv
from io import BytesIO
from bson import ObjectId 

from comprehend import get_pii_words

load_dotenv()

mongodb_uri = os.getenv("URI")
database_name = os.getenv("NAME")

app = FastAPI()

class Item(BaseModel):
    id: int
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

num_pages = None

@app.get("/")
async def read_root():
    print("READ ROOT")
    # Check if a PDF has been uploaded
    if num_pages is not None:
        return {"Number of pages in last uploaded PDF": num_pages}
    else:
        return {"message": "No PDF uploaded yet"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    print("i love women")
    global num_pages
    contents = await file.read()
    reader = PyPDF2.PdfReader(BytesIO(contents))

    # Store the number of pages in the global variable
    num_pages = len(reader.pages)
    text = await write_new_pdf(file)  # Await the coroutine here
    print(type(text))


    # call post with Item...
    item = Item(
        id=0,
        major_tag="6:59 PM",
        description="Coders!!",
        likes=137,
        pdf_file=text  # Store the PDF content in the pdf_file field
    )

    # Call the /create-item endpoint to insert the item into MongoDB
    result = await create_item(item)

    return {"filename": file.filename, "num_pages": num_pages}


async def write_new_pdf(file):
    db = MongoClient('mongodb://localhost:27017/').myDB
    fs = gridfs.GridFS(db)
    print("I love men!!")

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
async def read_item(item_id: str):
    try:
        # Manually convert the hexadecimal string to ObjectId
        item_id_obj = ObjectId(item_id)
    except bson.errors.InvalidId:
        # Handle the case when item_id is not a valid ObjectId
        raise HTTPException(status_code=400, detail="Invalid item_id")

    collection = db["items"]
    item = await collection.find_one({"_id": item_id_obj})
    
    if item:
        # Convert ObjectId to string for proper serialization
        item["_id"] = str(item["_id"])
        return item
    else:
        return {"message": "Item not found"}
    
# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     # Example: Fetch item details from MongoDB based on item_id
#     collection = db["items"]  # Replace "items" with your actual collection name
#     item = await collection.find_one({"item_id": item_id})
    
#     if item:
#         return item
#     else:
#         return {"message": "Item not found"}

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
async def delete_item(item_id: int):
    for item in db:
        if item.id == item_id:
            db.remove(item)
            return      
    raise HTTPException(status_code=404, detail=f"User with id: {item_id} does not exist.")
    
if client:
    print("Connected to MongoDB")