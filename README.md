# AI Interview Coach

An AI-powered interview preparation platform designed to help developers practice technical interview questions, improve their answers, and prepare for software engineering interviews.

## Project Goals

- Practice technical interview questions.
- Receive AI-assisted feedback on submitted answers.
- Track interview preparation progress.
- Build a full-stack application using modern backend and frontend technologies.

## Technology Stack

### Backend
- Python 3.13
- FastAPI
- Pydantic Settings
- SQLAlchemy
- PostgreSQL
- Pytest

### Frontend
- React
- TypeScript
- Vite

### AI and Development Tools
- Large Language Models (LLMs)
- Git and GitHub
- Docker
- GitHub Actions for CI/CD

## Project Structure

```text
ai-interview-coach/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   ├── tests/
│   ├── .env.example
│   ├── requirements.txt
│   └── README.md
├── frontend/
├── .gitignore
└── README.md
```

## Current Progress

- [x] Initialize the Git repository.
- [x] Set up the Python backend environment.
- [x] Create the initial FastAPI application.
- [x] Implement root and health-check endpoints.
- [x] Add configuration management using Pydantic Settings.
- [x] Write and pass initial backend tests.
- [ ] Configure PostgreSQL database integration.
- [ ] Develop backend API modules.
- [ ] Build the React frontend.
- [ ] Integrate AI-powered interview feedback.
- [ ] Add automated testing and CI/CD.

## Backend Setup

See [`backend/README.md`](backend/README.md) for instructions to configure and run the backend.

## Project Status

This project is under active development. Features will be added incrementally, with a focus on clean architecture, testing, and practical AI engineering skills.