import json

from bson import ObjectId
from fastapi.params import Query

from modules.gemini import call_gemini_api
from modules.calculation import calculate_correlation
from fastapi import FastAPI

# `backend dev main.py` to run the server
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import csv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

import json

from modules.gemini import call_gemini_api
from modules.calculation import calculate_correlation

# `backend dev main.py` to run the server
import json

from modules.gemini import call_gemini_api
from modules.calculation import calculate_correlation

# `backend dev main.py` to run the server
app = FastAPI()

uri = os.getenv("MONGODB_URI")
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://www.datadisco.study"],  # Allow only your Vue app's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/savefile/")
async def save_file(title: str = Form(...), description: str = Form(...), filename: str = Form(...)):

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

@app.delete("/deletefile/{id}")
async def delete_file(id: str):
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client["filestore"]
        collection = db["files"]

        result = collection.delete_one({"_id": ObjectId(id)})
        deleted_file = collection.find_one({"_id": ObjectId(id)})
        if deleted_file:
            file_path = f"uploaded_files/{deleted_file['id']}"
            if os.path.exists(file_path):
                os.remove(file_path)
        if result.deleted_count == 1:
            return {"message": "File deleted successfully!"}
        else:
            return {"message": "File not found!"}
    except:
        return {"message": "File not found!"}

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...), title: str = Form(...)):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["filestore"]
    collection = db["files"]
    document = {
        "title": title,
        "filename": file.filename
    }
    collection.insert_one(document)

    content = await file.read()
    decoded_content = content.decode("utf-8").splitlines()
    reader = csv.reader(decoded_content)
    data = [row for row in reader]
    file_location = f"uploaded_files/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(content)

    await save_file("test", "No description", file.filename)
    return {"filename": file.filename, "data": data}


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

def check_db_connection():
    uri = os.getenv("MONGODB_URI")
    if not uri:
        print("MONGODB_URI is not set in the .env file")
        return False

    client = MongoClient(uri, server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return True
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        return False

# Call the function to check the connection
check_db_connection()
    



check_db_connection()

@app.get("/getcorrelations")
async def get_correlations():
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["filestore"]
    collection = db["files"]
    # results =
    files = []
    for result in collection.find():
        try:
            files.append(
                {'filename': result['filename'], 'title': result['title'],
                 'id': str(result['_id'])})
        except:
            pass

    return files


@app.get("/gemini")
async def call_api():
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["filestore"]
    collection = db["files"]
    subPrompt = ''
    for result in collection.find():
        try:
            subPrompt += result['title'] + ', '
        except:
            pass
    response = call_gemini_api(subPrompt)
    try:
        text_content = response["candidates"][0]["content"]["parts"][0]["text"]
        json_string = text_content

        # Step 2: Remove the Markdown code block syntax
        json_string = json_string.strip("```json\n").strip("\n```")

        # Step 3: Parse the JSON string into a Python object
        parsed_data = json.loads(json_string)
        return parsed_data
    except:
        print('error')
        return {"message": response}
@app.get("/getcsvdata")
async def get_csv_data(filename: str = Query(...)):
    file_path = f"uploaded_files/{filename}"
    x = []
    y = []

    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the first row
            for row in reader:
                date, value = row
                try:
                    value = float(value)
                    x.append(date)
                    y.append(value)
                except ValueError:
                    return {"error": f"Invalid float value: {value}"}
    except Exception as e:
        return {"error": str(e)}

    return {"x": x, "y": y}