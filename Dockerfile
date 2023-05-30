# Base image with CUDA support
FROM python:3.11

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy app files
COPY src/ requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir torch 

# Expose Flask port
EXPOSE 5000

# Start Flask app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]