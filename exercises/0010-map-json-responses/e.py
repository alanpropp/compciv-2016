import json
import requests
import os

myfile = os.path.join("tempdata", "googlemaps", "stanford.json")
f = open(myfile, "r")
txt = f.read()
f.close()

mydict = json.loads(txt)
results = mydict['results']
for x in range(len(results)):
	current = results[x]
	print(current['formatted_address'], end = ';')
	geometry = current['geometry']
	location = geometry['location']
	print(location['lng'], end = ';')
	print(location['lat'])