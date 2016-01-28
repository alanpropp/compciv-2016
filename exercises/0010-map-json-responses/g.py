import json
import requests
import os

myfile = os.path.join("tempdata", "mapzen", "stanford.json")
f = open(myfile, "r")
txt = f.read()
f.close()

mydict = json.loads(txt)
features = mydict['features']
for x in range(len(features)):
	current=features[x]
	prop = current['properties']
	geo = current['geometry']
	print(prop['label'], end = ";")
	print(prop['confidence'], end = ";")
	print(geo['coordinates'][0],";",geo['coordinates'][1])	