from os.path import join, basename
import csv
YEAR = 2014
DATA_DIR = 'tempdata'
filename = join(DATA_DIR, 'wrangled2014.csv')
finalfile = open(filename, 'r')

count = 0
bigdatarow = []

reader = csv.reader(finalfile)
next(reader, None)

#Go through CSV file
for line in reader:
	if int(line[6]) >= 100 :
		bigdatarow.append(line)

ratios = [60, 70, 80, 90, 99]

total = len(bigdatarow)
print("Popular names in 2014 with gender ratio less than or equal to:")
for ratio in ratios:
	babies = 0
	for line in bigdatarow:
		if int(line[3]) <= ratio:
			babies += 1
	print("  " + str(ratio) + "%: " + str(babies) + "/" + str(total))