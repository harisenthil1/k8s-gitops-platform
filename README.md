# Kubernetes GitOps Platform

Minimal application used to demonstrate Kubernetes GitOps, CI/CD, security,
autoscaling, and observability.

## Local app

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
pytest -q
uvicorn app.main:app --reload
```

Open:

- http://localhost:8000/
- http://localhost:8000/health
- http://localhost:8000/ready
- http://localhost:8000/metrics

## Docker

```powershell
docker build -t k8s-gitops-demo:local .
docker run --rm -p 8000:8000 k8s-gitops-demo:local
```
