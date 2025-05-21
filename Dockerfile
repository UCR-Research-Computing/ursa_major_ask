# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application's source code to the working directory
COPY Ursa_Major_Ask .
COPY prompts.py .

# Make Ursa_Major_Ask executable
RUN chmod +x Ursa_Major_Ask

# Set environment variables
# The OPENAI_API_KEY will be passed at runtime
ENV OPENAI_API_KEY=""

# Define the command to run the application
CMD ["./Ursa_Major_Ask"]
