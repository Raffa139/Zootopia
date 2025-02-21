import requests
from environment import get_api_key

API_NINJAS = "https://api.api-ninjas.com/v1"
ANIMALS = "animals"
API_KEY = get_api_key()


def get_animal_data(animal):
    url = f"{API_NINJAS}/{ANIMALS}?name={animal}"
    response = requests.get(url, headers={"X-Api-Key": API_KEY})

    if response.status_code == 400:
        raise PermissionError(
            "Invalid or no API key provided. Make sure .env has valid API_KEY property.")

    if not response.status_code == 200:
        return []

    return response.json()
