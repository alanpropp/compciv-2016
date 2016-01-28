import json
import requests
import os

myfile = os.path.join("tempdata", "mapzen", "stanford.json")
f = open(myfile, "r")
txt = f.read()
f.close()

mydict = json.loads(txt)
curr_type = mydict['type']
print("Type: " + curr_type)
query = mydict['geocoding']['query']
print("text: " + query['text'])
print("size: " + str(query['size']))
print("boundary.country: " + query['boundary.country'])
