import os
import requests

mypath = os.path.join("tempdata", "googlemaps")
os.makedirs(mypath, exist_ok = True)
mypath = os.path.join("tempdata", "mapzen")
os.makedirs(mypath, exist_ok = True)

for x in range(2):
	print("---")
	url = ""
	mydirname = ""
	if x==0:
		url = "http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json"
		mydirname = os.path.join("tempdata", "googlemaps")
	else:
		url = "http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json"
		mydirname = os.path.join("tempdata", "mapzen")
	resp = requests.get(url)
	print("Downloading from: " + url)
	text = resp.text
	myfilename = "stanford.json"
	myfullfilename = os.path.join(mydirname, myfilename)
	outfile = open(myfullfilename, "w")
	print("Writing to: " + myfullfilename)
	outfile.write(text)
	split = text.splitlines()
	characters=0
	for y in text:
		characters+=1
	print("Wrote "+str(len(split))+" lines and "+
		str(characters)+" characters")
	outfile.close()
