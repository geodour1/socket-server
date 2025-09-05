# Use official lightweight Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port for WebSocket
EXPOSE 8765

# Run server
CMD ["python", "-u", "server.py"]