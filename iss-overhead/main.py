import requests
from datetime import datetime, timezone

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


#Your position is within +5 or -5 degrees of the ISS position.

def get_iss_lat_long():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude,iss_longitude



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now(timezone.utc)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

iss_lat,iss_long = get_iss_lat_long()

if abs(MY_LAT-iss_lat) <= 5.0 and abs(MY_LONG-iss_long) <= 5.0:
    #near me
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        print(f"Look up")



