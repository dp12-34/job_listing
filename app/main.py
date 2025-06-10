from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .job_provider import get_jobs

app = FastAPI(title="Job Listings for CS Graduates")
templates = Jinja2Templates(directory="templates")


@app.get("/jobs")
def read_jobs():
    """Return a list of job listings."""
    jobs = get_jobs()
    return jobs


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """Serve the frontend page."""
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
