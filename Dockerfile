# Use a Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONPATH=/app
ENV FLASK_APP=app:create_app
ENV FLASK_ENV=development

# Set the working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ app/
COPY tests/ tests/
COPY migrations/ migrations/
COPY pytest.ini .

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
