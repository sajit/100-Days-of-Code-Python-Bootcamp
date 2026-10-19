from pathlib import Path

import pandas


def get_weather_data_as_dict():
    """Return the weather data, locating the CSV beside this module."""
    csv_path = Path(__file__).with_name("weather_data.csv")
    data = pandas.read_csv(csv_path)
    return data.to_dict()
