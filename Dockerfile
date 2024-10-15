FROM python:3.12.5

# Set working directory
WORKDIR /app

# Install system dependencies for X11 and Nautilus
RUN apt-get update && apt-get install -y \
    libx11-6 \
    libxext-dev \
    libxrender-dev \
    xdg-utils \
    nautilus \
    x11-utils \
    libxinput-dev \
    desktop-file-utils \
    && rm -rf /var/lib/apt/lists/*

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files into the container
COPY . .
COPY Assets/ ./Assets/

# Set file permissions for Assets
RUN chmod -R 755 /app/Assets

# Run the application
CMD ["python", "VideoDownloader.py"]
