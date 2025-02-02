from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import csv
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

import json

from modules.gemini import call_gemini_api
from modules.calculation import calculate_correlation
from fastapi import FastAPI

# `fastapi dev main.py` to run the server
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow only your Vue app's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/savefile/")
async def save_file(title: str = Form(...), description: str = Form(...), filename: str = Form(...)):
    uri = os.getenv("MONGODB_URI")
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["filestore"]
    collection = db["files"]
    file = {
        "title": title,
        "description": description,
        "filename": filename
    }
    collection.insert_one(file)
    return {"message": "Data saved successfully!"}
@app.get("/")
async def root():
    # response = call_gemini_api()
    #
    # # print(response)
    # try:
    #     text_content = response["candidates"][0]["content"]["parts"][0]["text"]
    #     json_string = text_content
    #
    #     # Step 2: Remove the Markdown code block syntax
    #     json_string = json_string.strip("```json\n").strip("\n```")
    #
    #     # Step 3: Parse the JSON string into a Python object
    #     parsed_data = json.loads(json_string)
    #     return parsed_data
    # except:
    #     print('error')
    #     return response
    return {"message": "Hello World"}

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    decoded_content = content.decode("utf-8").splitlines()
    reader = csv.reader(decoded_content)
    data = [row for row in reader]
    file_location = f"uploaded_files/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(content)

    await save_file("test", "No description", file.filename)
    return {"filename": file.filename, "data": data}

def check_db_connection():
    uri = os.getenv("MONGODB_URI")
    client = MongoClient(uri, server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return True
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        return False

check_db_connection()

@app.post("/merge")
async def merge_files():
    return {"message": "Files merged successfully"}
