from os.path import join, basename
import csv
YEAR = 2014
DATA_DIR = 'tempdata'
filename = join(DATA_DIR, 'wrangled2014.csv')
finalfile = open(filename, 'r')

count = 0
reader = csv.reader(finalfile)
next(reader, None)
for line in reader:
	if count <5 and int(line[3]) < 60:
		print(line[1].ljust(8), line[2].rjust(3), line[3], line[6])
		count+=1