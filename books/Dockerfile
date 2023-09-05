FROM python:3.8

WORKDIR /app

COPY requirements_books.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI code for the "books" service into the image.
COPY books.py /app/

# Specify the command to run the FastAPI service
CMD ["uvicorn", "books:app", "--host", "0.0.0.0", "--port", "8001"]
