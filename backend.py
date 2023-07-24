import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
APIkey = os.getenv("API_KEY")


def get_data(place, days=None, d_type=None):
    api_call = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(api_call)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8*days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Minsk", days=3))