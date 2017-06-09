import requests
import json


def call_poke_api(name_pokemon):
	# pokemon api url
	url = 'http://pokeapi.co/api/v2/pokemon-species/' + name_pokemon

	# Get response from api
	response = requests.get(url)

	# Encode response in json
	json_response = json.loads(response.text)

	# Return only the description of the pokemon
	return json_response["flavor_text_entries"][1]["flavor_text"]
