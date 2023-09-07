# FastAPI Docker Kubernetes Project

This is a sample project demonstrating the setup and deployment of two FastAPI services (Books and Authors) using Docker and Kubernetes.
The project includes the following components:

- FastAPI applications for Books and Authors services.
- Docker containers for each service.
- Kubernetes deployment for scalability.
- Kubernetes Ingress for exposing the services as a single API.

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Docker Images](#docker-images)
- [Kubernetes Deployment & Ingress Setup](#kubernetes-deployment-and-ingress-setup)

## Project Overview

This project demonstrates how to containerize FastAPI applications, deploy them using Kubernetes and set up an Ingress to expose the services to external clients as a unified API.

## Prerequisites

Before running the project, ensure you have the following prerequisites:

- [Docker](https://docs.docker.com/get-docker/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- A Docker Hub account to push your Docker images.
- A code editor (e.g., VS Code) with Python and Kubernetes extensions (recommended).

## Project Structure

- `authors/`: FastAPI application for the Authors service.
- `books/`: FastAPI application for the Books service.
- `store_info.json`: Simple JSON data copied for each service.
- `Dockerfile`: Docker configuration for building the images.
- `requirements.txt`: Python dependencies for each service.
- `ingress/`: Kubernetes Ingress setup.

## Getting Started

1. Clone the repository to your local machine:

`git clone https://github.com/OrCHUK23/FastAPI-Docker-K8S.git`

`cd FastAPI-Docker-K8S`

2. Build Docker images for the Books and Authors services:

`docker build -t books-img -f books/Dockerfile.`

`docker build -t authors-img -f authors/Dockerfile .`

3. Create a Minikube cluster:

`minikube start -p my-cluster`

4. Deploy the pods services:

`kubectl apply -f authors_pod.yaml`

`kubectl apply -f books_pod.yaml`

4. Deploy the services to Kubernetes:

`kubectl apply -f authors_service.yaml`

`kubectl apply -f books_service.yaml`

5. Set up the Ingress:

`kubectl apply -f ingress.yaml`

6. Access the services at http://localhost (or the provided IP address).

## Usage
- The Books service is available at http://localhost/books/{book_name}.
- The Authors service is available at http://localhost/authors/{author_name}.
- Use curl or a web browser to interact with the services.

## Docker Images
Docker images for the Books and Authors services are available in my [DockerHub repositories](https://hub.docker.com/repositories/orchuk):

## Kubernetes Deployment and Ingress setup
The Kubernetes deployment and Ingress setup files are located in the main directory. You can adjust the number of replicas, resource limits, and other settings in these files.
The Ingress configuration exposes the services as a unified API under a single hostname.
