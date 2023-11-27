import requests

api_db = requests.get(url="https://opentdb.com/api.php", params={"amount": 10, "type": "boolean"})
api_db.raise_for_status()
question_data = api_db.json()["results"]
