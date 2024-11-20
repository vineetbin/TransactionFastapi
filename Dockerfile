FROM python:3.12

WORKDIR /app

# Copy requirements and install Python dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# EXPOSE the port
EXPOSE 8000
EXPOSE 5432
EXPOSE 5433

# Default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]