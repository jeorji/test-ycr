FROM python:3.11-slim

WORKDIR /app
COPY echo_server.py .
EXPOSE 8080


CMD ["python", "echo_server.py"]
