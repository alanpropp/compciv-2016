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
	add_comp = (current['address_components'])
	for y in range(len(add_comp)):
		current_dict = add_comp[y]
		print(current_dict['long_name'], end = "")
		if y != len(add_comp)-1:
			print('; ', end = '')
		else:
			print("")