import requests
import json

from typing import Dict, List


class Pokemon:
    def __init__(self, name: str, data: Dict[str, object]):
        self.name = name
        self.height = data["height"]
        self.weight = data["weight"]

    def __repr__(self) -> str:
        return f"Pokemon({self.name}, h={self.height}, w={self.weight})"


class PokemonEncoder(json.JSONEncoder):
    def default(self, pokemon: Pokemon) -> Dict[str, object]:
        return {
            "name": pokemon.name,
            "height": pokemon.height,
            "weight": pokemon.weight,
        }


class PokemonClient:
    def __init__(self):
        pass

    def get_pokemon_list(self, limit=10) -> List[Pokemon]:
        endpoint = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
        response = requests.get(endpoint)
        json_pokemon_list = response.json()

        pokemon_list = []
        for json_pokemon in json_pokemon_list["results"]:
            pokemon_list.append(
                Pokemon(
                    json_pokemon["name"], self.get_pokemon_details(json_pokemon["name"])
                )
            )
        return pokemon_list

    def get_pokemon_details(self, name: str) -> Pokemon:
        endpoint = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(endpoint)
        return response.json()


client = PokemonClient()
pokemon_list = client.get_pokemon_list()
print(pokemon_list)
print(json.dumps(pokemon_list[0], cls=PokemonEncoder))
