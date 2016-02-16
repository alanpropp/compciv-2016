import requests
import os
from operator import itemgetter

top10 = []
textfile = "ssa-babynames-nationwide-2014.txt"
myfile = os.path.join("tempdata", textfile)
outfile = open(myfile, "r")

top5_girls = []
top5_guys = []

for line in outfile:
	name, sex, babies = line.strip().split(',')
	baby = [name, sex, int(babies)]
	for letter in name:
		if letter.lower() == "x":
			if sex.lower() == "f":
				if len(top5_girls)<5:
					top5_girls.append(baby)
					top5_girls = sorted(top5_girls, key = itemgetter(2), reverse = True)
				elif baby[2] > top5_girls[4][2]:
					top5_girls[4] = baby
					top5_girls = sorted(top5_girls, key = itemgetter(2), reverse = True)
			elif sex.lower() == "m":
				if len(top5_guys)<5:
					top5_guys.append(baby)
					top5_guys = sorted(top5_guys, key = itemgetter(2), reverse = True)
				elif baby[2] > top5_guys[4][2]:
					top5_guys[4] = baby
					top5_guys = sorted(top5_guys, key = itemgetter(2), reverse = True)

print("Female")
for x in range(5):
	baby = top5_girls[x]
	print((str(x+1) + ". " + baby[0]).ljust(19), end="")
	print(str(baby[2]))

print("Male")
for x in range(5):
	baby = top5_guys[x]
	print((str(x+1) + ". " + baby[0]).ljust(19), end="")
	print(str(baby[2]).rjust(6))





