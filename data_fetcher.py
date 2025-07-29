import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'


def create_api_url(name):
    """
    Create the full API URL for fetching animal data.
    :param name: (str): The name of the animal to search for.
    :return: A tuple containing the formatted URL (str) and the animal name (str)
    """
    return API_URL.format(name), name


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    :param animal_name: (str): The name of the animal to fetch.
    :return list or None: A list of dictionaries if the request is successful, otherwise None.
    Example of returned data for one animal:
    {
    'name': ...,
    'taxonomy': {...},
    'locations': [...],
    'characteristics': {...}
    }
    """
    url, name = create_api_url(animal_name)
    response = requests.get(url, headers={'X-Api-Key': API_KEY})

    if response.status_code == requests.codes.ok:
      animals = response.json()  # 1. "animals" enthält deine Tierdaten (Liste von Dictionaries)
      return animals
    else:
        print("Error: fetching is not possible: ", response.status_code, response.text)
        return None

