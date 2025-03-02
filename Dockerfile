# Use the same base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the project files
COPY . /app/

# Create and activate a virtual environment
RUN python -m venv /app/venv
RUN /bin/bash -c "source venv/bin/activate && pip install --upgrade pip"
RUN pip install --no-cache-dir -r requirements.txt

# Ensure Django is installed
RUN python -m pip show django || (echo "Django is not installed!" && exit 1)

# Run Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
