import os
import requests
import string

textfile = "ssa-babynames-nationwide-2014.txt"
myfile = os.path.join("tempdata", textfile)
outfile = open(myfile, "r")

mydict = {}
for line in outfile:
	name, sex, babies = line.strip().split(",")
	last_letter = name[-1]
	if mydict.get(last_letter):
		mydict[last_letter] += int(babies)
	else:
		mydict[last_letter] = int(babies)

for letter in string.ascii_lowercase:
	print(letter, ":", mydict[letter])
