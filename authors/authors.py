import sys
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import json
import logging

app = FastAPI()

# Init store data as None.
store_data = None

# Configure the logging.
logging.basicConfig(level=logging.INFO, stream=sys.stdout, filemode="w")

# Add a line to the log file.
logging.info("This is a log for 'authors.py' errors")

# Load data from JSON when the application starts.
try: 
    with open("/data/store_info.json", "r") as json_file:
        store_data = json.load(json_file)
except FileNotFoundError as e:
    logging.error("Couldn't fetch the JSON file: %s", str(e))


@app.get("/")
async def root():
    return {"message": "Welcome to the Book Repository!"}


# Function handles "/author/name" get request.
@app.get("/author/{name}")
async def get_author(name: str):
    if store_data is None:
        raise HTTPException(status_code=500, detail="Data not available")
    
    # Find the author by name.
    author = None
    for author_data in store_data['authors']:
        if author_data['name'] == name.title():
            author = author_data
            break

    if author:
        # Find the books written by the author.
        author_books = []
        for book_data in store_data['books']:
            if book_data['author'] == name.title():
                author_books.append(book_data['title'])

        response_data = {
            "Name": author['name'],
            "Description": author['description'],
            "Books": author_books
        }
        return response_data, 200
    else:
        return {"message": "Author not found"}, 404


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)