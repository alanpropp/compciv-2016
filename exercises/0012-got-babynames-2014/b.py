import os
import requests

textfile = "ssa-babynames-nationwide-2014.txt"
myfile = os.path.join("tempdata", textfile)
outfile = open(myfile, "r")
babies = 0
for line in outfile:
	baby = line.split(",")
	babies+=int(baby[2])
print("There are", babies, "whose names were recorded in 2014")
