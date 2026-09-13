import requests
import os
from dotenv import load_dotenv

load_dotenv()
SERP_ENDPOINT = "https://serpapi.com/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.environ["SERP_API"]

    def check_flights(self, origin_city_code, destination_city_code):
        params = {
        "engine": "google_travel_explore",
        "departure_id": origin_city_code,
        "arrival_id": destination_city_code,
        "travel_duration": "2",
        "travel_mode": "1",
        "month":"0",
        "type": "1",
        "adults": "1",
        "currency": "EUR",
        "api_key": self.api_key,
        }

        response = requests.get(SERP_ENDPOINT, params=params)
        response.raise_for_status()
        data = response.json()
        return data
