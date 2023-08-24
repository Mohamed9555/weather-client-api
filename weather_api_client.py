import requests 
import json
class WeatherAPIClient:
    def __init__ (self, key):
        self.key =  key
        self._base_url = "http://api.weatherapi.com/v1"

    def get_current_temperature(self, city):
        destintaion = f"{self._base_url}/current.json"
        params = {
            "key": self.key,
            "q": city,
        }
        response = requests.get(destintaion, params)
        data = response.json(ه)
        return data["current"]["temp_c"]

    def get_temperature_after(self, city, days, hour = None):
        destintaion = f"{self._base_url}/forecast.json"
        params = {
            "key": self.key,
            "q": city,
            "days": days
        }
        response = requests.get(destintaion, params)
        data = response.json()
        if hour == None:
            return data["forecast"]["forecastday"][days-1]["day"]["maxtemp_c"] ### error 
        else:
            return data["forecast"]["forecastday"][days-1]["hour"][hour-1]["temp_c"] ### error 
  
    def get_lat_and_long(self,city):
        destintaion = f"{self._base_url}/current.json"
        params = {
            "key": self.key,
            "q": city,
        }
        response = requests.get(destintaion, params)
        data = response.json()
        lat = data["location"]["lat"]
        lon = data["location"]["lon"]
        return lat, lon

