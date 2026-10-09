# Base image that already contains the Python run-time
FROM python:3.12-slim

# Working directory inside the container
WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Document the port the app listens on
EXPOSE 5000

# Start the web server
CMD ["python", "app.py"]
