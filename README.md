# DataSnipper Tests

This project contains:
- API tests for [swapi.dev](https://swapi.dev)
- UI tests for [DataSnipper](https://www.datasnipper.com)

## Requirements
- Python 3.12+ (if running locally)
- Docker (if running in a container)

## Installation & Running Locally
1. Create/activate a virtual environment (optional):
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Install Playwright browsers:
   ```sh
   python -m playwright install chromium
   ```
4. Run tests:
   ```sh
   pytest tests -v
   ```

## Running with Docker
1. Build the Docker image:
   ```sh
   docker build -t datasnipper-tests .
   ```
2. Run the container:
   ```sh
   docker run --rm datasnipper-tests
   ```

   This will launch pytest inside the container and run all tests.