import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

rapid_api_key = os.environ.get("RAPID_API_KEY")


def find_actor_id(actor_name):
    url = "https://flixster.p.rapidapi.com/search"
    querystring = {"query": actor_name}
    headers = {
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": "flixster.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    # print(data)

    # Extractibg info from the API response

    for person in data.get("data", {}).get("search", {}).get("people", []):
        if person.get("name") == actor_name:
            return person.get("id")
    return None


def find_actor_profile(actor_id):
    url = "https://flixster.p.rapidapi.com/actors/detail"
    querystring = {"id": actor_id}
    headers = {
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": "flixster.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    response_profile = data.get("data", {}).get("person", {})
    actor_profile = {
        "name": response_profile.get("name"),
        "birthDate": response_profile.get("birthDate"),
        "headShotImage": response_profile.get("headShotImage"),
        "filmography": response_profile.get("filmography"),
    }
    return actor_profile


