# ✈️ Flight Deal Finder

A Python application that searches for cheap flights to selected destinations, compares them against target prices stored in Google Sheets, updates the sheet when a better deal is found, and sends email notifications automatically.

## 🚀 How It Works

The application follows this workflow:

1. Retrieves destinations and target prices from a Google Sheet using the **Sheety API**.
2. Searches for flights from Athens (`ATH`) to each destination using **SerpApi / Google Travel Explore**.
3. Searches for flexible travel dates within the next 6 months.
4. Finds the cheapest available flight for each destination.
5. Compares the flight price with the target price stored in the Google Sheet.
6. If a cheaper flight is found:

   * Updates the lowest price in the Google Sheet.
   * Sends an email notification with the flight details.

## 🛠 Technologies Used

* Python
* Requests
* REST APIs
* SerpApi / Google Travel Explore
* Sheety API
* Google Sheets
* SMTP Email
* python-dotenv
* Object-Oriented Programming (OOP)

## 📁 Project Structure

```text
flight-deal-finder/
│
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
├── notification_manager.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

### `main.py`

Controls the main application workflow and connects all project components.

### `data_manager.py`

Communicates with the Google Sheet through the Sheety API.

Responsibilities include:

* Retrieving destination data
* Retrieving notification users
* Updating the lowest flight price

### `flight_search.py`

Communicates with SerpApi to search for available flights using flexible travel dates.

### `flight_data.py`

Processes the flight API response and identifies the cheapest available flight.

### `notification_manager.py`

Sends email notifications when a flight is found below the target price.

## 📊 Google Sheet Structure

The destination sheet contains information such as:

```text
City | IATA Code | Lowest Price
Paris | CDG | 150
Rome | FCO | 100
Madrid | MAD | 120
```

The application compares the cheapest flight found with the `Lowest Price` value.

## 📧 Example Notification

```text
Low price alert!

Only 89 EUR to fly from ATH to FCO,
with 0 stop(s),
departing on 2026-10-12 and returning on 2026-10-19.
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/flight-deal-finder.git
```

Navigate to the project directory:

```bash
cd flight-deal-finder
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## 📦 Requirements

```text
requests
python-dotenv
```

## 🔐 Environment Variables

Create a `.env` file in the root directory.

Example:

```text
SERP_API=your_serpapi_key

SHEETY_USERNAME=your_sheety_username
SHEETY_PASSWORD=your_sheety_password
SHEETY_PRICES_ENDPOINT=your_prices_endpoint
SHEETY_USERS_ENDPOINT=your_users_endpoint

EMAIL_ADDRESS=your_email
EMAIL_PASSWORD=your_email_app_password
EMAIL_PROVIDER_SMTP_ADDRESS=your_smtp_address
```

The `.env` file is excluded from Git using `.gitignore` so API keys, passwords, and other sensitive information are not uploaded to GitHub.

## ▶️ Running the Application

Run:

```bash
python main.py
```

The application will check every destination in the Google Sheet and search for available flight deals.

If the cheapest available flight is below the target price, the application will automatically update the Google Sheet and send an email notification.

## 🧠 Skills Demonstrated

This project demonstrates:

* Working with REST APIs
* Processing JSON data
* API authentication
* Google Sheets integration
* HTTP requests
* Environment variables and secret management
* Email automation with SMTP
* Object-Oriented Programming
* Data processing and price comparison
* Error handling
* Multi-module Python project structure

## 🔒 Security

API keys, passwords, and credentials are stored in environment variables and are not included in the repository.

The `.env` file should never be committed to GitHub.

## 📌 Future Improvements

Possible future additions include:

* Scheduling automatic daily flight searches
* Adding additional departure airports
* Filtering by maximum number of stops
* Supporting different trip durations
* Adding airline information to email alerts
* Creating a graphical user interface
* Storing historical flight prices for price analysis
