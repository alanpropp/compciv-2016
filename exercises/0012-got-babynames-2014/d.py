import os
import requests

textfile = "ssa-babynames-nationwide-2014.txt"
myfile = os.path.join("tempdata", textfile)
outfile = open(myfile, "r")
count = 1
count2 = 1
for line in outfile:
	name, sex, babies = line.strip().split(",")
	if count < 6:
		if count==1:
			print("Top baby girl names")
		print(count,".", name, babies)
		count+=1
	elif sex == "M":
		if count2 < 6:
			if count2 ==1:
				print("")
				print("Top baby boy names")
			print(count2,".", name, babies)
			count2+=1



