import json

from modules.gemini import call_gemini_api
from modules.calculation import calculate_correlation
from fastapi import FastAPI

# `fastapi dev main.py` to run the server
app = FastAPI()


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
async def upload_file():
    return {"message": "File uploaded successfully"}


@app.post("/merge")
async def merge_files():
    return {"message": "Files merged successfully"}
