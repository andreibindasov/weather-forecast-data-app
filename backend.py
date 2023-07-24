import requests

APIkey = "3ea07bbd56db75de96a74a9fc3d26b21"


def get_data(place, days=None, d_type=None):
    api_call = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(api_call)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8*days
    filtered_data = filtered_data[:nr_values]
    if d_type == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if d_type == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Minsk", days=3, d_type="Temperature"))