import requests
from django.shortcuts import render

def pokemon_list(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=202"
    response = requests.get(url)
    data = response.json()
    pokemons = []

    for item in data["results"]:
        pokemon_data = requests.get(item["url"]).json()
        pokemons.append({
            "name": item["name"].capitalize(),
            "image": pokemon_data["sprites"]["front_default"],
            "id": pokemon_data["id"]
        })

    return render(request, "pokemon/list.html", {"pokemons": pokemons})


def pokemon_detail(request, pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)
    data = response.json()

    abilities = [ability["ability"]["name"].capitalize() for ability in data["abilities"]]

    context = {
        "name": data["name"].capitalize(),
        "image": data["sprites"]["front_default"],
        "abilities": abilities
    }
    
    return render(request, "pokemon/detail.html", context)
