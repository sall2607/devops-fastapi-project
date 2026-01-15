# DevOps FastAPI Project

## 📌 Project Overview
This project is a lightweight REST API built with FastAPI as part of a DevOps individual project.
The objective is to implement DevOps practices end-to-end, including CI/CD, containerization,
security scanning, observability, and Kubernetes deployment.

---

## 🛠️ Technologies Used
- Python 3.11
- FastAPI
- Docker
- GitHub Actions (CI/CD)
- Kubernetes (Minikube)
- Prometheus (Metrics)
- Bandit (SAST)
- OWASP ZAP (DAST)

---

## 📂 Project Structure
devops-fastapi-project/
├── app/
│ ├── init.py
│ └── main.py
├── tests/
│ ├── init.py
│ └── test_main.py
├── k8s/
│ ├── deployment.yaml
│ └── service.yaml
├── .github/workflows/
│ └── ci.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore



---

## 🚀 Run Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

2️⃣ Start the API
uvicorn app.main:app --reload

3️⃣ Available endpoints

   Health check: http://localhost:8000/health

   Metrics: http://localhost:8000/metrics

   Example endpoint: http://localhost:8000/items/1

🐳 Docker Usage
Build Docker image
docker build -t devops-fastapi .

Run Docker container
docker run -p 8000:8000 devops-fastapi

🔄 CI/CD Pipeline

The CI/CD pipeline is implemented using GitHub Actions and performs:

Code checkout

Dependency installation

Unit testing with pytest

Static security scan using Bandit

Docker image build and push to Docker Hub

📈 Observability

Metrics exposed at /metrics in Prometheus format

Structured logs generated for each HTTP request

Basic request tracing implemented via middleware

🔐 Security

- Static Analysis: Bandit
- Dynamic Analysis: OWASP ZAP
SAST: Bandit static code analysis

DAST: OWASP ZAP runtime security scanning

☸️ Kubernetes Deployment
Start Minikube
minikube start

Deploy application
kubectl apply -f k8s/

Access service
minikube service fastapi-service

📄 Author

Oulimata Sall


---

