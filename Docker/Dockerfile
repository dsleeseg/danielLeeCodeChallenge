# Use the official Python image from the Docker Hub
FROM python:3.9-slim


# Copy the requirements file into the container
COPY ../Docker/requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Specify the command to run the application
CMD ["python", "webApp.py"]

# Expose the port on which the app will run
EXPOSE 8080
