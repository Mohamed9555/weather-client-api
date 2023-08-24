from weather_api_client import WeatherAPIClient

########## Weather API ###############


client1 = WeatherAPIClient("78053d8fff3d470abf5161116232208")

print(
    f"currnet temprature in cairo: {client1.get_current_temperature('Cairo')}")

temp = client1.get_temperature_after("Cairo", 5, hour=None)
print(f"temprature in cairo fter 5 days: {temp}")

temp = client1.get_temperature_after("Cairo", 5, hour=2)
print(f"temprature in cairo fter 5 days in hour 2: {temp}")


lat, lon = client1.get_lat_and_long("Cairo")
print(f"Latitude and Longitude in cairo current day: {lat} {lon}")
