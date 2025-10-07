# docker_test

A simple Python Flask application containerized with Docker.

## Description

This is a minimal web application built with Flask that demonstrates:
- Running a Python application in a Docker container
- Using Docker Compose for deployment
- Basic health check endpoint

## Files

- `app.py` - Simple Flask web application
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker image configuration
- `deploy.yaml` - Docker Compose deployment configuration

## Usage

### Using Docker

Build the Docker image:
```bash
docker build -t docker_test_app .
```

Run the container:
```bash
docker run -p 5000:5000 docker_test_app
```

### Using Docker Compose

Deploy the application:
```bash
docker-compose -f deploy.yaml up
```

Or run in detached mode:
```bash
docker-compose -f deploy.yaml up -d
```

Stop the application:
```bash
docker-compose -f deploy.yaml down
```

## Access the Application

Once running, access the application at:
- Main page: http://localhost:5000
- Health check: http://localhost:5000/health

## Requirements

- Docker
- Docker Compose (optional, for using deploy.yaml)