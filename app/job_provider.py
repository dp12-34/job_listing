import os
from typing import List
import requests
from .models import JobListing

API_URL = "https://remotive.io/api/remote-jobs"


def get_jobs() -> List[JobListing]:
    """Fetch job listings from Remotive API filtered for computer science."""
    params = {"search": "computer science"}
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    jobs = []
    for item in data.get("jobs", []):
        jobs.append(
            JobListing(
                title=item.get("title"),
                company=item.get("company_name"),
                location=item.get("candidate_required_location"),
                url=item.get("url"),
                description=item.get("description"),
            )
        )
    return jobs
