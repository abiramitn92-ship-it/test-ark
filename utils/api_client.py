import requests

BASE_URL = "https://reqres.in/api"


class APIClient:

    @staticmethod
    def get_user(user_id):

        response = requests.get(
            f"{BASE_URL}/users/{user_id}"
        )

        return response

    @staticmethod
    def create_user(payload):

        response = requests.post(
            f"{BASE_URL}/users",
            json=payload
        )

        return response