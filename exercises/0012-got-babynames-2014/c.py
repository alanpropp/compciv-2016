import os
import requests

textfile = "ssa-babynames-nationwide-2014.txt"
myfile = os.path.join("tempdata", textfile)
outfile = open(myfile, "r")
Daenerys = 0
Khaleesi = 0
for line in outfile:
	name, sex, babies = line.strip().split(",")
	if name == "Daenerys":
		Daenerys+=int(babies)
	if "Khalees" in name or "Khaless" in name:
		Khaleesi +=int(babies)
print("Daenerys:", Daenerys)
print("Khaleesi", Khaleesi)