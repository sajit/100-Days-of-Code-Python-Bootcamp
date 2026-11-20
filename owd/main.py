import requests
import os
from itertools import islice


lat = 40.3101
lon = -75.1299
API_key = os.environ.get("OWM_KEY")
def get_forecast(lat:float,lon:float):
    if API_key is None:
        raise Exception

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    forecast = {}
    for condition in data["list"]:
        key = condition["dt_txt"]
        value = condition["weather"][0]["main"]
        forecast[key] = value
    

    return forecast

def rain_soon(weather_forecast:dict):
    #print(weather_forecast)
    first_four = dict(islice(weather_forecast.items(), 4))
    print(first_four)
    return "Rain" in first_four.values()
    
def main():
    print("Hello from owd!")
    #print(get_forecast(lat,lon))
    forecast = get_forecast(lat,lon)
    will_rain = rain_soon(forecast)
    print(f"It will rain soon {will_rain}")





if __name__ == "__main__":
    main()
