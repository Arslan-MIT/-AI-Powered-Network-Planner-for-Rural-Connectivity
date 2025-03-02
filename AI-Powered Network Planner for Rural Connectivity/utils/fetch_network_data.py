import requests
import config

def fetch_speedtest_data():
    response = requests.get(config.OOKLA_API_URL)
    if response.status_code == 200:
        return response.json()  # Process accordingly
    else:
        return None
