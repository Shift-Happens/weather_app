import requests
import toml
import ipapi

def load_config():
    with open("config.toml", "r") as f:
        return toml.load(f)

def get_location_from_ip():
    location = ipapi.location()
    return {
        'latitude': location.get('latitude'),
        'longitude': location.get('longitude'),
        'city': location.get('city')
    }

def get_weather_data(lat, lon):
    config = load_config()
    params = {
        'lat': lat,
        'lon': lon,
        'appid': config['api']['weather_api_key'],
        'units': 'metric'
    }
    response = requests.get(config['api']['base_url'], params=params)
    return response.json()