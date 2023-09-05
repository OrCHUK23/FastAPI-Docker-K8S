FROM python:3.8

WORKDIR /app

COPY requirements_authors.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI code for the "authors" service into the image.
COPY authors.py /app/

CMD ["uvicorn", "authors:app", "--host", "0.0.0.0", "--port", "8000"]
