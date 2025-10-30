import requests

BASE = "https://api.github.com/repos/octocat/Hello-World"

def test_status_is_200():
    r = requests.get(BASE, timeout=10)
    assert r.status_code == 200

def test_content_type_is_json():
    r = requests.get(BASE, timeout=10)
    assert "application/json" in r.headers.get("Content-Type","")

def test_minimum_keys_present():
    r = requests.get(BASE, timeout=10)
    data = r.json()
    for key in ["full_name", "private", "owner", "language"]:
        assert key in data

def test_owner_has_login_and_id():
    r = requests.get(BASE, timeout=10)
    owner = r.json().get("owner", {})
    assert isinstance(owner.get("login"), str) and owner.get("login")
    assert isinstance(owner.get("id"), int)

def test_rate_limit_header_exists():
    r = requests.get(BASE, timeout=10)
    assert r.headers.get("X-RateLimit-Limit") is not None
