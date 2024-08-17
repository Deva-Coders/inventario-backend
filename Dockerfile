
# Use the official Tiangolo FastAPI image with Python 3.9
FROM python:3.12.4-alpine

# Set the working directory
WORKDIR /zaiko
#run apt-get update && apt-get install -y libpq-dev gcc
# Copy the requirements file
COPY ./requirements.txt /zaiko/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /zaiko/requirements.txt

# Copy the rest of the application code
COPY ./zaiko . 

# Expose the port the app runs on
EXPOSE 80

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
