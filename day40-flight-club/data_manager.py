import os
import env
import requests


class DataManager:

    def __init__(self):
        env.create_env()
        self.sheet_get_endpoint = os.environ["SHEET_GET_ENDPOINT"]
        self.sheet_put_endpoint = os.environ["SHEET_PUT_ENDPOINT"]
        self.sheet_post_user_endpoint = os.environ["SHEET_POST_ENDPOINT"]
        token = os.environ["SHEETY_TOKEN"]
        self.auth_header = {
            "Authorization": "Bearer "+token,
        }

    def get_values(self):
        get_response = requests.get(url=self.sheet_get_endpoint, headers=self.auth_header)
        return get_response.json()["prices"]

    def put_code(self, data):
        for city in data:
            put_param = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            response = requests.put(url=self.sheet_put_endpoint+str(city["id"]), json=put_param, headers=self.auth_header)
            response.raise_for_status()

    def post_users(self, user_list):
        user = user_list[len(user_list)-1]
        post_param = {
            "users": {
                "firstName": user["first_name"],
                "lastName": user["last_name"],
                "email": user["email"],
            }
        }
        response = requests.post(url=self.sheet_post_user_endpoint, json=post_param, headers=self.auth_header)
        response.raise_for_status()
