# backend-service
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask==3.0.3
EXPOSE 5001
CMD ["python", "backend-service.py"]