import requests

req = requests.get('https://swapi.dev/api/starships')
data = req.json().get("results")
for item in data:
    if item["name"] == "Millennium Falcon":
        name = item["name"]
        speed = item["max_atmosphering_speed"]
        starship_class = item["starship_class"]
        pilots_info = item["pilots"]
        print(f"Name: {name}, speed: {speed}, class: {starship_class}. \nPilots info: ")
        for url in item["pilots"]:
            response = requests.get(url)
            data_1 = response.json()
            pilot_name = data_1.get("name")
            height = data_1.get("height")
            mass = data_1.get("mass")
            planet = data_1.get("homeworld")
            print(f"Pilot name: {pilot_name}, height: {height}, mass: {mass}, planet: {planet}")

