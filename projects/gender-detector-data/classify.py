import requests
from os import makedirs
from os.path import join
import csv
from gender import detect_gender

DATA_DIR = "tempdata"
DATA = "nobel_wrangled.csv"
CLASSIFIED = "classified_data.csv"
DATA_PATH = join(DATA_DIR, DATA)
CLASSIFIED_DATA_PATH = join(DATA_DIR, CLASSIFIED)
all_names = []

#Extracts usable name 
def extract_usable_name(name):
	name = name.strip()
	result = ""
	for n in range(len(name)):
		if name[n] == " ":
			if result[1] == ".":
				result = ""
			else:
				return result.strip(" ")
		result+=name[n]
	return result.strip(" ")

#Actually goes through CSV file and reads it
wrangled_file = open(DATA_PATH, 'r', encoding="latin1")
my_reader = csv.reader(wrangled_file, skipinitialspace=True)
next(my_reader, None) #Skips headers
for line in my_reader:
	year = line[0]
	category = line[1]
	name = line[2]
	country = line[3]
	field = line[4]
	motivation = line[5]
	usable_name = extract_usable_name(name)
	gender = detect_gender(usable_name)['gender']
	ratio = detect_gender(usable_name)['ratio']
	namesdict = {'year': year, 'category': category, 'name': name,
	'country': country, 'field': field, 'motivation': motivation, 
	'gender': gender, 'ratio': ratio,'usable_name': usable_name}
	all_names.append(namesdict)


#Creates new file
HEADERS = ['year', 'category', 'name' , 'country' , 'field', 'motivation', 'gender', 'ratio', 'usable_name']
wfile = open(CLASSIFIED_DATA_PATH, 'w')
wcsv = csv.DictWriter(wfile, fieldnames=HEADERS)
# write the headers row
wcsv.writeheader()

for entry in all_names:
	wcsv.writerow(entry)
# the end...close the file
wfile.close()

