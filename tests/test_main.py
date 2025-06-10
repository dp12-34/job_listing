from fastapi.testclient import TestClient

from app.main import app


def test_jobs_endpoint(monkeypatch):
    sample_jobs = [
        {
            "title": "Software Engineer",
            "company": "Example Corp",
            "location": "Remote",
            "url": "https://example.com/job/1",
            "description": "Job description",
        }
    ]

    def fake_get_jobs():
        return sample_jobs

    monkeypatch.setattr("app.job_provider.get_jobs", fake_get_jobs)

    client = TestClient(app)
    response = client.get("/jobs")
    assert response.status_code == 200
    assert response.json() == sample_jobs


def test_jobs_endpoint_handles_error(monkeypatch):
    import requests

    def fail_get_jobs():
        raise requests.RequestException("failed")

    monkeypatch.setattr("app.job_provider.get_jobs", fail_get_jobs)
    client = TestClient(app)
    response = client.get("/jobs")
    assert response.status_code == 200
    assert response.json() == []
