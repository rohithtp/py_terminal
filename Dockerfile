FROM python:3.12-slim

# Create a non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

# Change ownership of the app to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "terminal_web/main.py"]
