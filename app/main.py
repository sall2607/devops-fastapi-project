from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, generate_latest
import time
import logging
import json

app = FastAPI()

REQUEST_COUNT = Counter(
    "request_count", "Total requests", ["method", "endpoint"]
)

REQUEST_TIME = Histogram(
    "request_latency_seconds", "Request latency"
)

logging.basicConfig(level=logging.INFO)

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    latency = time.time() - start

    REQUEST_COUNT.labels(
        request.method, request.url.path
    ).inc()
    REQUEST_TIME.observe(latency)

    logging.info(json.dumps({
        "method": request.method,
        "path": request.url.path,
        "status": response.status_code,
        "latency": latency
    }))

    return response

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@app.get("/metrics")
def metrics():
    return generate_latest()
