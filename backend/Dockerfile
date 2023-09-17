# Use an official Python runtime as base image
FROM python:3.9-slim-buster

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install Flask

# Expose port
EXPOSE 5000

# Run app.py when the container launches
CMD ["flask", "run"]