# Use an official Python runtime as a base image
FROM python:3.9-slim-buster

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Optional: Set environment variables for MongoDB (can also be set in docker-compose.yaml)
# ENV MONGO_URI=mongodb://username:password@mongo:27017/db_name

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install both Flask and PyMongo
RUN pip install Flask pymongo

# Expose port
EXPOSE 5000

# Run app.py when the container launches
CMD ["flask", "run"]
