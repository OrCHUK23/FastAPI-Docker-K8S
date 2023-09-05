FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copy code and JSON into the image.
COPY books.py /app/
COPY store_info.json /data/

# Specify the command to run the FastAPI service
CMD ["uvicorn", "books:app", "--host", "0.0.0.0", "--port", "8001"]
