# test_api.py
import requests
import pytest
BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def base_url():
    return BASE_URL

def test_get_posts(base_url):
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0

@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_get_post_by_id(base_url, post_id):
    response = requests.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == post_id

def test_create_post(base_url):
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{base_url}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == payload['title']
    assert data['body'] == payload['body']
    assert data['userId'] == payload['userId']
