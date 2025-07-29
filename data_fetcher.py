import requests
import os
from dotenv import load_dotenv
load_dotenv()  # Loads the environment variables

API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'

def create_api_url(name):
    return API_URL.format(name), name


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    url, name = create_api_url(animal_name)
    response = requests.get(url, headers={'X-Api-Key': API_KEY})

    if response.status_code == requests.codes.ok:
      animals = response.json()  # 1. "animals" enthält deine Tierdaten (Liste von Dictionaries)
      return animals
    else:
        print("Error: fetching not possible: ", response.status_code, response.text)
        return None

