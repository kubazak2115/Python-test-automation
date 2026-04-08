import pytest
import requests
import jsonschema
from jsonschema import validate

API_URL = "https://jsonplaceholder.typicode.com"

#SCHEMA

POST_SCHEMA = {
    "type": "object",
    "required": ["id", "userId", "title", "body"],
    "properties": {
        "id":     {"type": "integer"},
        "userId": {"type": "integer"},
        "title":  {"type": "string"},
        "body":   {"type": "string"}
    },
    "additionalProperties": False
}

COMMENT_SCHEMA = {
    "type": "object",
    "required": ["id", "postId", "name", "email", "body"],
    "properties": {
        "id":     {"type": "integer"},
        "postId": {"type": "integer"},
        "name":   {"type": "string"},
        "email":  {"type": "string"},
        "body":   {"type": "string"}
    },
    "additionalProperties": False
}

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "username", "email"],
    "properties": {
        "id":       {"type": "integer"},
        "name":     {"type": "string"},
        "username": {"type": "string"},
        "email":    {"type": "string"}
    }
}

#POST SCHEMA TESTS

@pytest.mark.smoke
@pytest.mark.api
def test_get_single_post_schema():
    """ should match schema when fetching single post """
    post_id = 67
    response = requests.get(f"{API_URL}/posts/{post_id}")
    data = response.json()
    validate(instance=data, schema=POST_SCHEMA)

@pytest.mark.regression
@pytest.mark.api
def test_get_all_posts_match_schema():
    """ should match schema when fetching all posts """
    response = requests.get(f"{API_URL}/posts")
    data = response.json()
    for post in data:
        validate(instance=post, schema=POST_SCHEMA)

@pytest.mark.regression
@pytest.mark.api
def test_post_id_is_integer():
    """ should have integer id when creating new post """
    response = requests.get(f"{API_URL}/posts/6")
    data = response.json()
    assert isinstance(data["id"], int)

@pytest.mark.regression
@pytest.mark.api
def test_post_fields_are_not_empty():
    """ should have non-empty fields when fetching post """
    response = requests.get(f"{API_URL}/posts/6")
    data = response.json()
    assert data["title"] != ""
    assert data["body"] != ""

#COMMENT SCHEMA TESTS

@pytest.mark.smoke
@pytest.mark.api
def test_get_comment_for_post_match_schema():
    """ should match schema when fetching comments for a post """
    response = requests.get(f"{API_URL}/comments/6")
    data = response.json()
    validate(instance=data, schema=COMMENT_SCHEMA)

@pytest.mark.regression
@pytest.mark.api
def test_comment_email_format():
    """ should have valid email format in comment """
    response = requests.get(f"{API_URL}/comments/6")
    data = response.json()
    assert "@" in data["email"] and "." in data["email"]

#USER SCHEMA TESTS

@pytest.mark.smoke
@pytest.mark.api
def test_user_matches_schema():
    """ should match schema when fetching user by id """
    user_id = 7
    response = requests.get(f"{API_URL}/users/{user_id}")
    data = response.json()
    validate(instance=data, schema=USER_SCHEMA)

@pytest.mark.regression
@pytest.mark.api
def test_all_users_have_email():
    """ should have email field for all users """
    response = requests.get(f"{API_URL}/users")
    users = response.json()
    for user in users:
        assert "email" in user
        assert "@" in user["email"] and "." in user["email"]