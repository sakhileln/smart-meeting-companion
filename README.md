# 🧠 Smart Meeting Companion
An AI-powered mobile app that helps users turn meeting audio into actionable insights. Upload or record meetings, get automated transcripts, summaries, and key action items—all in one place.

## 📌 Overview

**Smart Meeting Companion** is a full-stack application with a Flutter frontend and a FastAPI backend. It uses AI models to transcribe meeting audio and extract meaningful insights like summaries, decisions, and action points.

## 🚀 Features
* 🎹 Upload or record meeting audio
* ✍️ Automatic transcription using Whisper
* 🧠 Summarization and action item extraction via AI
* 🔐 User authentication with JWT
* 🧾 View and manage past meeting summaries
* 📊 Monitoring and logging for backend services
* ☁️ Containerized with Docker, deployable with Kubernetes

## 🧰 Tech Stack
| Layer          | Technology                                       |
| -------------- | ------------------------------------------------ |
| **Frontend**   | Flutter (Dart)                                   |
| **Backend**    | FastAPI (Python)                                 |
| **Database**   | SQLite (can be upgraded to Postgres)             |
| **AI Models**  | Whisper for transcription, LLM for summarization |
| **Auth**       | JWT, password hashing (`passlib`)                |
| **Monitoring** | Prometheus + Grafana                             |
| **DevOps**     | Docker, Kubernetes (Minikube/Kind)               |

## 📂 Project Structure
```
smart-meeting-companion/
├── backend/
│   ├── app/
│   │   ├── main.py            # FastAPI entry point
│   │   ├── models.py          # SQLAlchemy models
│   │   ├── schemas.py         # Pydantic schemas
│   │   ├── crud.py            # DB operations
│   │   ├── transcriber.py     # Audio transcription (Whisper)
│   │   ├── summarizer.py      # AI-based summarization
│   │   └── auth.py            # User auth and JWT
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── lib/
│   │   ├── main.dart
│   │   ├── screens/
│   │   ├── services/
│   ├── pubspec.yaml
│   └── Dockerfile
├── k8s/                        # Kubernetes manifests
│   ├── backend-deployment.yaml
│   ├── frontend-deployment.yaml
│   ├── db-deployment.yaml
│   ├── ingress.yaml
│   └── monitoring/
├── docker-compose.yml
└── README.md
```

## 💠 Getting Started
### 1. Prerequisites
* Python 3.10+
* Flutter SDK
* Docker & Docker Compose
* Optional: Minikube or Kind for Kubernetes

### 2. Backend (Local Dev)
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Frontend (Flutter App)
```bash
cd frontend
flutter pub get
flutter run
```

### 4. Docker Compose (Full Stack)
```bash
docker-compose up --build
```

## 🔐 Security
* Passwords stored with `bcrypt` (via `passlib`)
* JWT-based login system
* API protected with role-based access control

## 📊 Monitoring & Observability
* FastAPI instrumented with Prometheus exporter
* Grafana dashboards (preconfigured in `k8s/monitoring`)
* Health check endpoints for readiness/liveness

## 📦 Deployment with Kubernetes
1. Start local cluster (e.g. Minikube)
2. Apply manifests:
```bash
kubectl apply -f k8s/
```
3. Access app via configured Ingress or LoadBalancer

## 🧠 AI Details
* **Transcription**: OpenAI Whisper or `faster-whisper`
* **Summarization**: HuggingFace Transformers (e.g., `bart-large-cnn`) or OpenAI API
* Optional: local LLM using `llama.cpp` or `ollama`

## 📃 Database Schema (Simplified)
* `User`: id, email, hashed\_password
* `Meeting`: id, user\_id, title, datetime, audio\_file, transcript, summary
* `ActionItem`: id, meeting\_id, description, status

## 🧹 Future Enhancements
* Real-time transcription and summarization
* Team collaboration & sharing
* Full-text search with vector embeddings
* Voice assistant integration

## 🤝 Contact
- Sakhile III  
- [LinkedIn Profile](https://www.linkedin.com/in/sakhile-)
- [GitHub Profile](https://github.com/sakhileln)
