FROM python:3

WORKDIR /app/machine_learning_client

COPY requirements.txt ./

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgl1-mesa-glx libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/machine_learning_client

EXPOSE 5001

ENV MONGODB_URI="mongodb://mongo:27017/"
ENV MONGODB_DATABASE="proj4"

CMD ["python", "app.py", "python3"]