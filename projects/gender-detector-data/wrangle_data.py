import requests
from os import makedirs
from os.path import join
import csv


DATA_DIR = 'tempdata'
DATA_PATH = join(DATA_DIR, 'nobel_wrangled.csv')
DATA_PATH_NON_WRANGLED = join(DATA_DIR, 'nobel.csv')
print("Creating", DATA_PATH)

WRANGLED_HEADERS = ['year', 'category', 'name' , 'country' , 'field', 'motivation']

namesdict = {}

with open(DATA_PATH_NON_WRANGLED, 'r') as oldfile:
	my_reader = csv.reader(oldfile, delimiter=',')
	next(my_reader, None)
	for line in my_reader:
		print(line)
		year = line[0]
		category = line[1]
		name = line[2]
		country = line[5]
		field = line[8]
		motivation = line[10]
		namesdict[name] = {'year': year, 'category': category, 'name': name, 'country': country, 'field': field, 'motivation': motivation}

# let's create the new file to write to
wfile = open(DATA_PATH, 'w')
# turn it into a DictWriter object, and tell it what the fieldnames are
wcsv = csv.DictWriter(wfile, fieldnames=WRANGLED_HEADERS)
# write the headers row
wcsv.writeheader()

for entry in namesdict:
    wcsv.writerow(entry)
# the end...close the file
wfile.close()