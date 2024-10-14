# Flask Docker Application

This is a simple Flask-based application that exposes three endpoints (`GET /foo`, `POST /hello`, and `GET /kill`). The application is containerized using Docker, and the Docker image can be built and run easily.

## Features

- **GET /foo**: Returns a simple string response `bar`.
- **POST /hello**: Takes a JSON body with a `name` field and returns a personalized greeting.
- **GET /kill**: Terminates the running Docker container.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
  - [Endpoints](#endpoints)
- [Building and Running the Docker Image](#building-and-running-the-docker-image)
- [DockerHub](#dockerhub)
- [License](#license)

## Getting Started

### Prerequisites

- **Docker Desktop**: Install [Docker Desktop](https://www.docker.com/products/docker-desktop) to build and run the containerized application.
- **Python 3.x**: Make sure you have Python installed for local development.
- **Flask**: Flask will be used as the web framework.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/arashkp/flask-docker-app.git
   cd flask-docker-app
