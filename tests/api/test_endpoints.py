import pytest
import requests

API_URL = "https://jsonplaceholder.typicode.com"

#GET

@pytest.mark.smoke
@pytest.mark.api
def test_get_all_posts_returns_200():
    """ should return 200 status code when fetching all posts """
    response = requests.get(f"{API_URL}/posts")
    assert response.status_code == 200

@pytest.mark.smoke
@pytest.mark.api
def test_get_all_posts_returns_100_items():
    """ should return 100 posts when fetching all posts """
    response = requests.get(f"{API_URL}/posts")
    data = response.json()
    assert len(data) == 100

@pytest.mark.smoke
@pytest.mark.api
def test_get_single_post_returns_200():
    """ should return 200 status code when fetching single post """
    post_id = 67
    response = requests.get(f"{API_URL}/posts/{post_id}")
    data = response.json()
    assert data["id"] == post_id

@pytest.mark.regression
@pytest.mark.api
def test_get_nonexistent_post_returns_404():
    """ should return 404 status code when fetching nonexistent post """
    post_id = 67676767
    response = requests.get(f"{API_URL}/posts/{post_id}")
    assert response.status_code == 404

@pytest.mark.regression
@pytest.mark.api
def test_get_posts_returns_json_content_type():
    """ should return json response when fetching posts """
    response = requests.get(f"{API_URL}/posts/1")
    assert "application/json" in response.headers["Content-Type"]

@pytest.mark.regression
@pytest.mark.api
@pytest.mark.parametrize("post_id", [6, 7, 67, 101])
def test_get_post_by_id_returns_200(post_id):
    """ should return 200 status code when fetching post by id """
    response = requests.get(f"{API_URL}/posts/{post_id}")
    if post_id <= 100:
        assert response.status_code == 200
    else:
        assert response.status_code == 404

@pytest.mark.regression
@pytest.mark.api
def test_get_comments_for_post_returns_200():
    """ should return 200 status code when fetching comments for a valid post """
    response = requests.get(f"{API_URL}/posts/7/comments")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

@pytest.mark.regression
@pytest.mark.api
def test_get_all_users_returns_10_items():
    """ should return 10 users when fetching all users """
    response = requests.get(f"{API_URL}/users")
    data = response.json()
    assert len(data) == 10

#POST

@pytest.mark.smoke
@pytest.mark.api
def test_post_new_post_returns_201():
    """ should return 201 status code when creating new post """
    payload = {
        "title": "cristiano",
        "body": "ronaldo",
        "userId": 7
    }
    response = requests.post(f"{API_URL}/posts", json=payload)
    assert response.status_code == 201

@pytest.mark.smoke
@pytest.mark.api
def test_post_response_contains_sent_data():
    """ should return created post data in response """
    payload = {
        "title": "cristiano",
        "body": "ronaldo",
        "userId": 7
    }
    response = requests.post(f"{API_URL}/posts", json=payload)
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

@pytest.mark.regression
@pytest.mark.api
def test_post_response_contains_new_id():
    """ should return created post with an id in response """
    payload = {
        "title": "cristiano",
        "body": "ronaldo",
        "userId": 7
    }
    response = requests.post(f"{API_URL}/posts", json=payload)
    data = response.json()
    assert "id" in data
    assert data["id"] is not None

#PUT

@pytest.mark.smoke
@pytest.mark.api
def test_put_update_post_returns_200():
    """ should return 200 status code when updating existing post """
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 7
    }
    response = requests.put(f"{API_URL}/posts/1", json=payload)
    assert response.status_code == 200

@pytest.mark.regression
@pytest.mark.api
def test_put_response_contains_updated_data():
    """ should return updated post data in response """
    payload = {
        "id": 1,
        "title": "updated title",
        "body": "updated body",
        "userId": 7
    }
    response = requests.put(f"{API_URL}/posts/1", json=payload)
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

#DELETE

@pytest.mark.smoke
@pytest.mark.api
def test_delete_post_returns_200():
    """ should return 200 status code when deleting existing post """
    post_id = 67
    response = requests.delete(f"{API_URL}/posts/{post_id}")
    assert response.status_code == 200

@pytest.mark.regression
@pytest.mark.api
def test_delete_nonexistent_post_returns_200():
    """ should return 200 status code when deleting nonexistent post """
    post_id = 67676767
    response = requests.delete(f"{API_URL}/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data == {}