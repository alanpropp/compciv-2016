import os
import requests
import string

textfile = "ssa-babynames-nationwide-2014.txt"
myfile = os.path.join("tempdata", textfile)
outfile = open(myfile, "r")

mydict = {"M": {}, "F": {}}
for line in outfile:
	name, sex, babies = line.strip().split(",")
	last_letter = name[-1]
	nested_dict = mydict.get(sex)
	if nested_dict.get(last_letter):
		nested_dict[last_letter]+=int(babies)
	else:
		nested_dict[last_letter] = int(babies)

print("letter".ljust(8), end = "")
print("F".rjust(8), end = "")
print("M".rjust(8))
for x in range(24):
	print("-", end = "")
print("")
for letter in string.ascii_lowercase:
	print(letter.ljust(8), end = "")
	F = mydict.get("F")
	F_babies = F[letter]
	F_str = str(F_babies)
	print(F_str.rjust(8), end = "")
	M = mydict.get("M")
	M_babies = M[letter]
	M_str = str(M_babies)
	print(M_str.rjust(8))
