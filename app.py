from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from collections import deque
import re

# ✅ Initialize FastAPI app first
app = FastAPI()

# ✅ Setup template rendering
templates = Jinja2Templates(directory="templates")


# ✅ Define data model for request
class CompareRequest(BaseModel):
    min_capacity: int
    max_capacity: int
    urls: str


# ✅ FIFO Algorithm with hit/miss tracking and trace
def fifo_metrics(capacity, pages):
    cache = deque()
    cache_misses = 0
    cache_hits = 0
    trace = []

    for page in pages:
        if page in cache:
            cache_hits += 1
            trace.append(f"Request {page} → ✅ Cache Hit → Cache = {list(cache)}")
        else:
            cache_misses += 1
            evicted = None
            if len(cache) == capacity:
                evicted = cache.popleft()
            cache.append(page)
            if evicted:
                trace.append(f"Request {page} → ❌ Cache Miss → Evicted {evicted} → Cache = {list(cache)}")
            else:
                trace.append(f"Request {page} → ❌ Cache Miss → Added {page} → Cache = {list(cache)}")

    total_requests = len(pages)
    hit_ratio = round(cache_hits / total_requests, 2) if total_requests else 0
    miss_ratio = round(cache_misses / total_requests, 2) if total_requests else 0

    return {
        "cache_size": capacity,
        "cache_misses": cache_misses,
        "cache_hits": cache_hits,
        "hit_ratio": hit_ratio,
        "miss_ratio": miss_ratio,
        "trace": trace
    }


# ✅ Route for homepage
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ✅ Route to compare results
@app.post("/compare_fifo")
def compare_fifo(request_data: CompareRequest):
    min_c = request_data.min_capacity
    max_c = request_data.max_capacity
    # urls = [url.strip() for url in request_data.urls.split(",") if url.strip()]
    # inside your route:
    raw = request_data.urls.strip()
    # split on any number of commas or whitespace
    urls = [u for u in re.split(r'[,\s]+', raw) if u]

    results = {}
    for cap in range(min_c, max_c + 1):
        metrics = fifo_metrics(cap, urls)
        results[cap] = metrics

    return {"comparative_results": results}
