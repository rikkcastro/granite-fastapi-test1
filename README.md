# FastAPI Text Generation with Granite-1B Base Model

This project provides a FastAPI-based web application for text generation using the **Granite-1b-base** model. The API allows you to send text input and receive a generated continuation or response based on the input.

## Features

- **Text Generation**: Generate human-like text responses based on an input prompt.
- **Granite-1B Model**: Uses the Granite-1B-base model from HuggingFace for generating the text.
- **FastAPI**: FastAPI framework to quickly build the web API and serve the model.
- **Uvicorn**: ASGI server for running the FastAPI app.
- **Docker**: Optional Docker setup for containerized deployment.

## Setup

### Prerequisites

- Python 3.8+
- `pip` (Python package installer)
- `git` (for cloning the repository)
- `virtualenv` (recommended for setting up a virtual environment)

### Installing the dependencies

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rikkcastro/granite-fastapi-test.git
   cd granite-fastapi-test
