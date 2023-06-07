# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire repository to the working directory
COPY . .

# Expose the Application Port
EXPOSE 5000

# Set the command to run your application
CMD ["python", "app.py"]
