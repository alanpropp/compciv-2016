import requests
import os
from operator import itemgetter

top10 = []
textfile = "ssa-babynames-nationwide-2014.txt"
myfile = os.path.join("tempdata", textfile)
outfile = open(myfile, "r")
for line in outfile:
	name, sex, babies = line.strip().split(',')
	baby = [name, sex, int(babies)]
	if len(top10) < 10:
		top10.append(baby)
	elif baby[2] > top10[9][2]:
		top10[9] = baby
		top10 = sorted(top10, key=itemgetter(2), reverse = True)

for n in range(10):
	baby = top10[n]
	print(n+1, ".", baby[0], ",", baby[1], ",", baby[2])
