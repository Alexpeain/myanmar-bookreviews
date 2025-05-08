FROM python:3.11-alpine

# Install system dependencies required for psycopg2 and potentially others
RUN apk update && apk add --no-cache postgresql-dev build-base

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your Django project code
COPY . /app/

# Expose the port your Django app will run on (usually 8000)
EXPOSE 8000

# Default command to run your Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]