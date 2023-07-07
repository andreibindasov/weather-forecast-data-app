import requests

APIkey = "3ea07bbd56db75de96a74a9fc3d26b21"


def get_data(place, days=None, d_type=None):
    api_call = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(api_call)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(place="Minsk"))