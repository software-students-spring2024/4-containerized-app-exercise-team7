# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install pipenv
RUN pip install pipenv

# Install any needed packages specified in Pipfile
RUN pipenv install --system --deploy

# Make port 80 available to the world outside this container
EXPOSE 5000

# If you have any environment variables, add them here
# ENV MONGO_URI=your_mongo_uri
# ENV MONGO_DBNAME=your_mongo_dbname
# ENV FLASK_PORT=your_flask_port

# Run app.py when the container launches
CMD ["python", "app.py"]
