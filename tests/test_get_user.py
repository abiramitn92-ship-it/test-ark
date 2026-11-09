from utils.api_client import APIClient


def test_get_user():

    response = APIClient.get_user(2)

    assert response.status_code == 200

    body = response.json()

    assert body["data"]["id"] == 2

    assert body["data"]["email"] == "janet.weaver@reqres.in"