# Weather Client API

This project provides a Python client for interacting with a weather API to retrieve weather information based on user input.

## Getting Started

To use this weather client API, you'll need to have Python installed on your machine.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Mohamed9555/weather-client-api.git
   cd weather-client-api
   pip install -r requirements.txt

## Usage

Get your API key:
  Visit the weather API provider's website (https://www.weatherapi.com).
  Sign up and obtain an API key.
  
Create a .env file in the project directory: 

    client1 = WeatherAPIClient("API key")
    
    print(f"currnet temprature in cairo: {client1.get_current_temperature('Cairo')}")
  
    temp = client1.get_temperature_after("Cairo", 5, hour=None)
    print(f"temprature in cairo after 5 days: {temp}")
    
    temp = client1.get_temperature_after("Cairo", 5, hour=2)
    print(f"temprature in cairo after 5 days in hour 2: {temp}")
    
    
    lat, lon = client1.get_lat_and_long("Cairo")
    print(f"Latitude and Longitude in cairo current day: {lat} {lon}")

  python weather_client.py



