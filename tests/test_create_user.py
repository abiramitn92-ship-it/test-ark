from utils.api_client import APIClient

def test_create_user():

    payload = {
        "name": "Abirami",
        "job": "QA Engineer"
    }

    response = APIClient.create_user(payload)
    print(response.json())

    assert response.status_code == 201

    body = response.json()

    assert body["name"] == "Abirami"