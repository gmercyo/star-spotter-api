import requests

def find_actor_id(actor_name):
    url = "https://flixster.p.rapidapi.com/search"
    querystring = {"query": actor_name}
    headers = {
        "X-RapidAPI-Key": "8a01746374msh2ece6217940931cp1c4fc2jsne1b46198292b",
        "X-RapidAPI-Host": "flixster.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    # print(data)

    # Extractibg info from the API response

    for person in data.get('data', {}).get('search', {}).get('people', []):
        if person.get('name') == actor_name:
            return person.get('id')
    return None

actor_id = find_actor_id("Jennifer Aniston")
if actor_id is not None:
    print(f"Jennifer Aniston's ID: {actor_id}")
else:
    print("Actor not found")
