# AI Interview Coach — Backend

A backend API for an AI-powered interview preparation platform, built with Python and FastAPI.

## Tech Stack

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL with Psycopg
- Pydantic Settings
- Pytest

## Project Structure

```text
backend/
├── app/
│   ├── api/
│   │   └── v1/
│   ├── core/
│   │   └── config.py
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   │   └── ai/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── .env.example
├── requirements.txt
└── README.md
```

## Setup

### 1. Activate the virtual environment

From the backend directory, run:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 3. Configure environment variables

Copy the example file:

```powershell
Copy-Item .env.example .env
```

Update `.env` with your local configuration when required. Never commit real credentials or secrets.

### 4. Run the API

```powershell
uvicorn app.main:app --reload
```

The API runs locally at `http://127.0.0.1:8000`.

### 5. API documentation

- Swagger UI: `http://127.0.0.1:8000/docs`
- Root endpoint: `http://127.0.0.1:8000/`
- Health endpoint: `http://127.0.0.1:8000/health`

### 6. Run tests

```powershell
python -m pytest -v
```

## Current Status

- FastAPI application initialized.
- Centralized application configuration implemented.
- Root and health endpoints implemented.
- Environment variable loading verified.
- Automated tests added for endpoints and configuration.

## Planned Development

- PostgreSQL database integration.
- Database models and schemas.
- Versioned API routes.
- Interview question management.
- AI-powered interview feedback.
- Authentication and user management.
- Front