

from fastapi import FastAPI

# `fastapi dev main.py` to run the server
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/uploadfile/")
async def upload_file():
    return {"message": "File uploaded successfully"}

@app.post("/merge")
async def merge_files():
    return {"message": "Files merged successfully"}