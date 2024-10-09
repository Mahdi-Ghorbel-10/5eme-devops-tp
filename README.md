# Python Calculator Project with GitHub Actions and Docker

This project demonstrates a simple calculator application built with Python and automated using GitHub Actions for CI/CD. The calculator supports basic operations such as addition, subtraction, multiplication, division, and calculating the average of a list. It is also containerized with Docker for easy deployment.

## Features

- **Calculator Operations**: Perform addition, subtraction, multiplication, division, and calculate the average of a list of numbers.
- **Automated Testing**: Uses PyTest to run unit tests on every pull request to ensure code quality.
- **Docker Containerization**: The application is built and published as a Docker image using GitHub Actions.
- **CI/CD with GitHub Actions**: Automatically builds and pushes Docker images on push to the `main` branch and runs tests on every pull request.

## Project Structure

```
Calculatrice/
│
├── calculatrice/                # Directory for the main module
│   └── main.py                  # Main Python file containing the Calculator class
├── requirements.txt             # Python dependencies
├── tests/                       # Directory for unit tests
│   └── test_main.py             # Unit tests for the Calculator class
└── .github/                     # Directory for GitHub Actions workflows
    └── workflows/
        ├── docker-build.yml     # GitHub Actions workflow for building and pushing Docker images
        └── test.yml             # GitHub Actions workflow for running tests on pull requests
```

## Getting Started

### Prerequisites

- Python 3.9 or later
- Docker installed on your machine
- A Docker Hub account
- GitHub repository with `DOCKER_USERNAME` and `DOCKER_PASSWORD` set as secrets

### Setting Up the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BorchaniSalma/Calculatrice.git
   cd Calculatrice
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python calculatrice/main.py
   ```

4. **Run Tests Locally**:
   ```bash
   pytest tests
   ```

### Docker Usage

1. **Build the Docker Image**:
   ```bash
   docker build -t docker-username/python-github-actions:latest .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -it  docker-password/python-github-actions:latest
   ```

3. **Push the Docker Image to Docker Hub**:
   Make sure you are logged in to Docker:
   ```bash
   docker login -u docker-username -p docker-password
   docker push docker-username/python-github-actions:latest
   ```

### GitHub Actions

The project uses GitHub Actions for CI/CD. Below are the workflows used:

- **`docker-build.yml`**: This workflow builds and pushes the Docker image to Docker Hub whenever there is a push to the `main` branch.
- **`test.yml`**: This workflow runs unit tests using `pytest` whenever a pull request is created.

### Setting Up GitHub Secrets

To allow GitHub Actions to push Docker images to Docker Hub, set the following secrets in your GitHub repository:

1. Go to **Settings** > **Secrets and variables** > **Actions**.
2. Click **New repository secret**.
3. Add the following secrets:
   - **`DOCKER_USERNAME`**: Your Docker Hub username.
   - **`DOCKER_PASSWORD`**: Your Docker Hub password or access token.

### CI/CD Workflows

1. **Docker Build and Push**:
   - Automatically triggered on every push to the `master` branch.
   - Builds a Docker image from the `Dockerfile` and pushes it to Docker Hub.
   - Workflow file: `.github/workflows/docker-build.yml`.

2. **Run Tests**:
   - Automatically triggered on every pull request to the `master` branch.
   - Runs tests using `pytest` to validate the functionality of the code.
   - Workflow file: `.github/workflows/test.yml`.

