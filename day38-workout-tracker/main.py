import os
import env
import requests
from datetime import datetime

env.create_env()

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

GENDER = "female"
WEIGHT = 50
HEIGHT = 165
AGE = 22

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

nutrix_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=header)
nutrix_response.raise_for_status()
result = nutrix_response.json()


auth_header = {
    "Authorization": "Bearer " + SHEETY_TOKEN,
}

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": round(exercise["duration_min"], 0),
            "calories": round(exercise["nf_calories"], 0),
        }
    }
    response = requests.post(url=sheet_endpoint, json=sheet_params, headers=auth_header)
    response.raise_for_status()
