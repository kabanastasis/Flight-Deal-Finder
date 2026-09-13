class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, nr_stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.nr_stops = nr_stops


def find_cheapest_flight(data):
    if data is None or (not data.get("flights")):
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    all_flights = data["flights"]
    out_date = data["start_date"]
    return_date = data["end_date"]

    lowest_price = float("inf")
    cheapest_flight = None

    for flight in all_flights:
        # Exception handling - json has data but flight is missing 'price'. Skip.
        try:
            price = flight["price"]
        except KeyError:
            print("--- No price available for flight. ---")
            continue

        if price < lowest_price:
            lowest_price = price
            departure = flight["departure_airport"]["id"]
            arrival = flight["arrival_airport"]["id"]
            nr_stops = flight["number_of_stops"]

            cheapest_flight = FlightData(lowest_price, departure, arrival, out_date, return_date, nr_stops)
    if cheapest_flight is None:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    return cheapest_flight
