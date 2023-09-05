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
logging.info("This is a log for 'books.py' errors")

# Load data from db.json when the application starts
try: 
    with open("/data/store_info.json", "r") as json_file:
        store_data = json.load(json_file)
except FileNotFoundError as e:
    logging.error("Couldn't fetch the JSON file: %s", str(e))


# Function handles "/books/name" get request.
@app.get("/books/{book_name}")
def get_book(book_name: str):
    if store_data is None:
        raise HTTPException(status_code=500, detail="Data not available")

    # Find the book by title name.
    book = None
    for book_data in store_data['books']:
        if book_data['title'] == book_name.title():
            book = book_data
            break

    # Check if a book was found.
    if book:  
        response_data = {
            "title": book['title'],
            "book details": book['book details'],
            "author": book['author']
        }
        return response_data, 200
    else:
        return {"message": "Book not found"}, 404


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8001)