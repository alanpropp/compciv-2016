import os
import requests

textfile = "ssa-babynames-nationwide-2014.txt"
myfile = os.path.join("tempdata", textfile)
outfile = open(myfile, "r")

boys = 0
girls = 0
for line in outfile:
	name, sex, babies = line.strip().split(",")
	if sex == "F":
		girls += int(babies)
	elif sex == "M":
		boys += int(babies)
print("F:", girls)
print("M:", boys)