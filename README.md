# LeadGen – AI-Powered Lead Generation System

LeadGen is an AI-driven web application that generates **Ideal Customer Profile (ICP) questions** and identifies **relevant companies** based on a given persona and industry.  
The system uses a **local LLM via Ollama**, an asynchronous task queue with **Celery**, and a **Flask** web backend, all fully **Dockerized**.

---

## Features

- Generate ICP questions using a local LLM (Ollama – LLaMA 3.2 1B)
- Asynchronous question generation using Celery & Redis
- Company discovery based on persona and industry
- Clean web UI built with Flask templates
- Fully containerized using Docker & Docker Compose

---

##  Tech Stack

- **Backend:** Flask (Python)
- **LLM:** Ollama (LLaMA 3.2 – 1B model)
- **Task Queue:** Celery
- **Message Broker:** Redis
- **Database:** SQLite
- **Frontend:** HTML, CSS (Jinja2 templates)
- **Containerization:** Docker, Docker Compose

---
##  How to Run the Project

1. Clone the Repository
```bash
git clone https://github.com/your-username/leadgen.git
cd leadgen
2.Start All Services
bash
Copy code
docker compose up --build

### This will start:
Flask backend (localhost:5000)
Celery worker
Redis server
Ollama LLM server

### Application Flow
1.User enters persona and industry
2.Flask sends request to Celery
3.Celery calls Ollama LLM to generate ICP questions
4.Questions are displayed to the user
5.User submits answers
6.Relevant companies are fetched and displayed

### Author
Developed by Kaviya M
