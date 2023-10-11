FROM ubuntu:20.04


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    python3-pip \
    libgl1-mesa-glx \
    make \
    wget \
    ffmpeg \
    libsm6 \
    libxext6


WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD make run_app
