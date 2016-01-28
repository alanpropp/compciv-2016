import json
import requests
import os

myfile = os.path.join("tempdata", "googlemaps", "stanford.json")
f = open(myfile, "r")
txt = f.read()
f.close()

mydict = json.loads(txt)
print(mydict['status'])
