from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import csv
import pymongo as pymongo


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow only your Vue app's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
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
    return {"filename": file.filename, "data": data}

@app.post("/uploadmongodb/")
async def upload(title: str, description: str):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["fastapi"]
    collection = db["files"]
    data = {"title": title, "description": description, "file_name": "file_name"}
    collection.insert_one(data)
    return {"message": "File uploaded successfully"}