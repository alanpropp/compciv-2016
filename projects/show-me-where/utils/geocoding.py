import requests
import json

def geocode(location):
	"""
	Attempts to geocode a location string using Mazpen Search API

	Input:
	--------------
	Geocode expects as input a strong that represents some kind of
	geographical location. For example: "Stanford, CA", or "New York
	City"

	It also expects the variable 'CREDS_FILE' to point to an existing
	file that contains a valid Mapzen Search key, as given by the user

	Function:
	--------------
	Geocode will open and read CREDS_FILE to get the API key.

	It will then call the Mapzen Search API via an HTTP request, using
	the API key, and the user-provided 'location' string as the 'text'
	parameter.

	It then deserializes the Mapzen Search response into a dictionary,
	using the JSON library.

	Finally, it creates a dictionary

	Returns:
	--------------
	- query_text: the 'location' string provided by the user
	- lable: the string label that Mapzen provides in describing the
	found location
	- confidence: a float representing the confidence value that Mapzen
	has in its result
	- latitude: a float representing the latitude coordinate
	- longitude: a float representing the longitude coordinate
	- status: "OK", a string that indicates a result was found. Else, None

	"""

	txt = fetch_mapzen_response(location)
	mydict = parse_mapzen_response(txt)
	mydict['query_text'] = location
	return mydict

def fetch_mapzen_response(location):
	"""
	'location' is a string that will be passed in to Mapzen API for 
	geocoding

	This function returns a text string containing JSON-formatted
	data from Mapzen
	"""
	mykey = read_mapzen_credentials()
	myparams = {'text': location, 'api_key': mykey}
	url = "https://search.mapzen.com/v1/search?"
	resp = requests.get(url, params=myparams)
	return resp.text

def parse_mapzen_response(txt):
	"""
	txt is a string containing JSON-formatted text from Mapzen's API

	This function returns a dictionary containing the useful key/value
	pairs from the most relevant result.
	"""
	dictionary = {}
	data = json.loads(txt)
	if data['features']:
		dictionary['status'] = 'OK'
		current = data['features'][0]
		props = current['properties']
		dictionary['confidence'] = props['confidence']
		dictionary['label'] = props['label']

		coordinates = current['geometry']['coordinates']
		dictionary['longitude'] = coordinates[0]
		dictionary['latitude'] = coordinates[1]
	else:
		dictionary['status'] = None

	return dictionary

def read_mapzen_credentials():
	creds_filename = 'creds_mapzen.txt'
	keytxt = open(creds_filename).read().strip()
	return keytxt
