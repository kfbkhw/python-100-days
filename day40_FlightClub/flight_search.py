import os
import requests
from datetime import datetime, timedelta
from flight_data import FlightData


class FlightSearch:

    def __init__(self):
        self.kiwi_endpoint = "https://api.tequila.kiwi.com"
        self.search_endpoint = "/v2/search"
        api = os.environ["FLIGHT_API_KEY"]
        self.header = {
            "apikey": api,
        }

    def find_code(self, city):
        code_endpoint = "/locations/query"
        query = {
            "term": city,
            "location_types": "city"
        }
        code_response = requests.get(url=self.kiwi_endpoint + code_endpoint, params=query, headers=self.header)
        code = code_response.json()["locations"][0]["code"]
        return code

    def search_flights(self, city_code, origin, curr):
        date_from = datetime.now().date() + timedelta(days=1)
        date_to = datetime.now().date() + timedelta(days=180)
        search_param = {
            "fly_from": origin,
            "fly_to": city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": curr,
        }
        ticket_response = requests.get(url=self.kiwi_endpoint+self.search_endpoint, params=search_param, headers=self.header).json()["data"][0]
        data = FlightData(
            price=ticket_response["price"],
            currency=curr,
            from_city=ticket_response["cityFrom"],
            from_code=ticket_response["flyFrom"],
            to_city=ticket_response["cityTo"],
            to_code=ticket_response["flyTo"],
            start_date=ticket_response["route"][0]["local_departure"].split("T")[0],
            end_date=ticket_response["route"][1]["local_departure"].split("T")[0],
        )
        return data
