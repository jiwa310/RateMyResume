import PyPDF2
import os 

from typing import Union, Optional
from uuid import UUID
from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()

mongodb_uri = os.getenv("URI")
database_name = os.getenv("NAME")

app = FastAPI()

class Item(BaseModel):
    id: Optional[UUID] = int
    major_tag: str
    description: str
    likes: int
    

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

@app.post("/create-item")
async def create_item(item: Item):
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
async def delete_item(item_id: int):
    for item in db:
        if item.id == item_id:
            db.remove(item)
            return      
    raise HTTPException(status_code=404, detail=f"User with id: {item_id} does not exist.")
    
if client:
    print("Connected to MongoDB")