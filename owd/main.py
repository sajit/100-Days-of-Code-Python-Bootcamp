import requests
import os

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
    forecast = []
    for condition in data["list"]:
        key = condition["dt_txt"]
        value = condition["weather"][0]["main"]
        forecast.append({key : value})
    
    
    return forecast
def main():
    print("Hello from owd!")
    print(get_forecast(lat,lon))



if __name__ == "__main__":
    main()
