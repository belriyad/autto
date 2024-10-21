# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Create a non-root user and group
RUN groupadd -r myuser && useradd -r -g myuser myuser

# Change ownership of the application directory to the non-root user
RUN chown -R myuser:myuser /app

# Switch to the non-root user
USER myuser

# Expose port 8080
EXPOSE 8080

# Define environment variable
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Run the application
CMD ["python3", "main.py"]
