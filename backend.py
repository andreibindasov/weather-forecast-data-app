import requests

APIkey = see_vars


def get_data(place, days=None, d_type=None):
    api_call = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(api_call)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(place="Minsk"))