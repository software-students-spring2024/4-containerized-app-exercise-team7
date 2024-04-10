FROM python:3.9



RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y



# Copy your Python files into the container
COPY . /app

# Set the working directory
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run your Python script
CMD ["python", "app.py"]
