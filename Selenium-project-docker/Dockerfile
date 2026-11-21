# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies and Chrome
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get update \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire test-suite folder
COPY pytests/ ./test-suite/

# Create directory for test reports
RUN mkdir -p reports

# Execute all Pytest test cases
CMD ["pytest", "-v", "--junitxml=reports/results.xml", "test-suite/"]
