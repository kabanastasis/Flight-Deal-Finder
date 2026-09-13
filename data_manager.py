import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.username = os.environ['SHEETY_USERNAME']
        self.password = os.environ['SHEETY_PASSWORD']
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self.authorization = HTTPBasicAuth(self.username, self.password)

    def get_prices_data(self):
        response = requests.get(self.prices_endpoint, auth=self.authorization)
        response.raise_for_status()
        prices_data = response.json()["prices"]
        return prices_data

    def get_users_data(self):
        response = requests.get(self.users_endpoint, auth=self.authorization)
        response.raise_for_status()
        users_data = response.json()["users"]
        return users_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{self.prices_endpoint}/{row_id}",
            json=new_data,
            auth=self.authorization
        )
