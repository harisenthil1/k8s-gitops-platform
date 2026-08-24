import os
import time
from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="Kubernetes GitOps Demo")

REQUESTS = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "path", "status"],
)

LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["path"],
)

@app.middleware("http")
async def metrics_middleware(request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    elapsed = time.perf_counter() - start

    REQUESTS.labels(
        method=request.method,
        path=request.url.path,
        status=response.status_code,
    ).inc()
    LATENCY.labels(path=request.url.path).observe(elapsed)

    return response

@app.get("/")
def root():
    return {
        "service": "k8s-gitops-demo",
        "status": "running",
        "version": os.getenv("APP_VERSION", "dev"),
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/work")
def work():
    # Intentional CPU work so we can later demonstrate HPA.
    total = 0
    for i in range(1_000_000):
        total += i * i
    return {"status": "complete", "result": total}

@app.get("/error")
def error():
    return Response(content="intentional demo error", status_code=500)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
