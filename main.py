from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
from pprint import pprint

data_manager = DataManager()
prices_data = data_manager.get_prices_data()
users_data = data_manager.get_users_data()
users_emails = [row["whatIsYourEmai?"] for row in users_data]

flight_search = FlightSearch()

notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "ATH"

for destination in prices_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        )

    cheapest_flight = find_cheapest_flight(flights)
    pprint(f"{destination['city']}: {cheapest_flight.price} EUR")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        if cheapest_flight.nr_stops == 0:
            message = f"Low price alert! Only {cheapest_flight.price} EUR to fly direct " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only {cheapest_flight.price} EUR to fly " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"with {cheapest_flight.nr_stops} stop(s) " \
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        notification_manager.send_email(email_list=users_emails, subject="Low price alert!", message=message)
