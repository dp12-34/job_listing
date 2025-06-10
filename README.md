# Job Listing API

This project provides a simple FastAPI application that serves job listings for computer science graduates. It includes a small frontend to display jobs fetched from a remote API (Remotive). If the provider is unreachable, the API returns an empty list instead of failing.

## Setup

1. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Run the development server:

```bash
uvicorn app.main:app --reload
```

3. Open `http://localhost:8000` in your browser to see the frontend.

## Testing

Run the tests using pytest:

```bash
pytest
```
