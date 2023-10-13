# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY app.py .

# Copy the templates directory into the container
COPY templates/ /app/templates/

# Copy the static (CSS) directory into the container
COPY static/ /app/static/

# Expose a port for communication (optional)
EXPOSE 5000

# Install any required dependencies (Flask, in this case)
RUN pip3 install --default-timeout=100 flask
RUN pip3 install --default-timeout=100 jsonify
RUN pip3 install --default-timeout=100 mysql-connector-python
RUN pip3 install --default-timeout=100 requests
# Define the command to run the Python script
CMD ["python", "app.py"]
