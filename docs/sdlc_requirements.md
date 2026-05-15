# Software Requirements Specification: AI Quote Generator

## 1. Purpose

The AI Quote Generator is a small web application that displays inspirational quotes and an automatically generated visual background. The project demonstrates meta-software development by using an AI-assisted Jupyter Notebook to generate software artefacts such as backend code, frontend code, UML documentation, and SDLC documentation.

## 2. Scope

The system provides a browser-based interface where users can view an automatically generated image and request a new inspirational quote. The Flask backend serves the webpage, returns quote data through a JSON API, and retrieves generated image content from the Pollinations image API.

## 3. Stakeholders

- End user: interacts with the website and requests quotes.
- Developer: maintains the Flask application, Docker configuration, and CI/CD workflow.
- Teaching assessor: evaluates evidence of meta-software development, deployment, and automation.

## 4. Functional Requirements

- The system shall serve a homepage at `/`.
- The system shall display at least one automatically generated image.
- The system shall provide a `/api/quote` endpoint that returns quote data in JSON format.
- The system shall allow users to request a new quote from the frontend without reloading the page.
- The system shall provide a `/generated-image` route that retrieves image content from Pollinations API.
- The system shall include generated UML documentation describing the request flow.
- The system shall include generated SDLC documentation describing requirements and assumptions.

## 5. Non-Functional Requirements

- The web application should be simple to run locally using Python.
- The Docker container should expose port 5000 and run the Flask application.
- The frontend should be responsive and readable on common screen sizes.
- The application should avoid committing real API keys or credentials.
- The CI/CD workflow should validate installation and Docker build steps.

## 6. User Stories

- As a user, I want to open the webpage and see a visually appealing generated image.
- As a user, I want to click a button and receive an inspirational quote.
- As a developer, I want the project to be containerised so it can run consistently in different environments.
- As an assessor, I want to see evidence that AI was used to generate software artefacts and documentation.

## 7. Acceptance Criteria

- Opening `/` returns a valid HTML page.
- Opening `/api/quote` returns a JSON response containing a `quote` field.
- Opening `/generated-image` returns image content when the external service is reachable.
- The project contains `app.py`, `templates/index.html`, `diagram.puml`, `Dockerfile`, `requirements.txt`, and `.github/workflows/main.yml`.
- The Notebook includes an AI calling function and automated generation steps for code and documentation.

## 8. System Architecture

The frontend is a single HTML page rendered by Flask. JavaScript sends asynchronous requests to the Flask backend. The backend returns quote data as JSON and proxies image generation through Pollinations API. Docker packages the application, and GitHub Actions validates dependency installation and container build.

## 9. Deployment Assumptions

- Python dependencies are installed from `requirements.txt`.
- The application runs on port 5000.
- The container uses `python:3.11-slim`.
- External internet access is available when retrieving generated images.

## 10. Risks

- The external image API may be unavailable or slow.
- Network restrictions may prevent image retrieval.
- Accidentally committing real API keys would create a security risk.
- Minimal automated testing may reduce confidence in future changes.
