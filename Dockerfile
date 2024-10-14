# Use an official Python runtime as a parent image
FROM python:3.9-buster

# Install necessary dependencies
USER root
RUN apt-get update && apt-get install -y \
	build-essential \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# Create a non-root user and switch to it
RUN useradd -m myuser

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /home/myuser/app
COPY --chown=myuser:myuser requirements.txt .

# Switch to root to create a virtual environment and install dependencies
USER root
RUN python -m venv venv && \
	pip install --no-cache-dir -r requirements.txt

# Change ownership of the virtual environment to the non-root user
RUN chown -R myuser:myuser venv

# Switch back to the non-root user
USER myuser

# Copy the rest of the application code into the container at /home/myuser/app
COPY --chown=myuser:myuser . .

# Expose port 8080
EXPOSE 8080

# Define environment variable
ENV VIRTUAL_ENV=venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Run the application
CMD ["python", "scrap.py"]
