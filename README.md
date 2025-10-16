# Tiny API QA with Python + pytest

Tiny API quality checks on a public endpoint using Python and `pytest` — asserts status code, content type, and a few schema keys.  
**Green checks or it didn’t happen.**

## Why this exists
Recruiter‑friendly micro‑demo to show you can validate an API without claiming “automation engineer.” Fast to skim, easy to run.

## Setup
```bash
# from project root
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Run
```bash
pytest -q
```

Expected: all tests pass. If one fails, either GitHub changed something or you’re offline — that’s okay; the point is the structure.

## Files
- `test_public_api.py` — 5 small tests (status, headers, minimal schema, owner fields, rate limit header)
- `requirements.txt` — pytest + requests
- `.gitignore` — ignores venv, caches, pyc files
- `LICENSE` — MIT

## Suggested repo meta
- **Name:** `tiny-api-qa-pytest`
- **Description:** Tiny API quality checks with Python + pytest: status, headers, and schema assertions on a public endpoint.
- **Topics:** `pytest`, `api-testing`, `quality-assurance`, `portfolio`

## License
MIT — do what you want, attribution appreciated.
