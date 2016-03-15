import requests
from os import makedirs
from os.path import join
import csv

DATA_DIR = "tempdata"
DATA = "classified_data.csv"
DATA_PATH = join(DATA_DIR, DATA)
all_names = []

print()
print('-'*70)
print()
#Goes through CSV file and reads it
data_file = open(DATA_PATH, 'r', encoding="latin1")
my_reader = csv.reader(data_file, skipinitialspace=True)
next(my_reader, None) #Skips headers
for line in my_reader:
	year = line[0]
	category = line[1]
	name = line[2]
	country = line[3]
	field = line[4]
	motivation = line[5]
	gender = line[6]
	ratio = line[7]
	usable_name = line[8]
	namesdict = {'year': year, 'category': category, 'name': name,
	'country': country, 'field': field, 'motivation': motivation, 
	'gender': gender, 'ratio': ratio,'usable_name': usable_name}
	all_names.append(namesdict)
data_file.close()

#Total male/female ratio analysis
print('Total male/female ratio for Nobel Prize winners over the years:')
total_male = 0
total_female = 0
total_NA = 0
for x in range(len(all_names)):
	entry = all_names[x]
	if entry['gender'] == 'M':
		total_male+=1
	elif entry['gender'] == 'F':
		total_female+=1
	elif entry['gender'] == 'NA':
		total_NA+=1
print('Male/female ratio = ', round(total_male/total_female, 3), " (", total_male, 
	" males and ", total_female, " females)", sep = '')
print('There were also', total_NA, 'names for which we could not determine gender')
print()
print('-'*70)
print()

#Decade-based male/female ratio analysis
print('Decade-based male/female ratio Nobel Prize winners:')
decades = ["190", "191", "192", "193", "194", "195", "196", "197", "198", "199", "200", "201"]
for decade in decades:
	males = 0
	females = 0
	for x in range(len(all_names)):
		entry = all_names[x]
		if entry['year'][0:3]==decade:
			if entry['gender'] == 'M':
				males+=1
			elif entry['gender'] == 'F':
				females+=1
	curr_decade = decade + "0s"
	if females == 0:
		print("In the", curr_decade, "there were", males, "male and no female Nobel prizewinners")
	else:
		print("In the ", curr_decade, " the male/female ratio was ", round(males/females, 3), " (", males,
			" males and ", females, " females)", sep='')
print()
print('-'*70)
print()

#Category-based male/female ratio analysis
print('Category-based male/female ratio Nobel Prize winners:')
categories = {}
for x in range(len(all_names)):
	entry = all_names[x]
	curr_category = entry['category']
	if not categories.get(curr_category):
		if entry['gender'] == 'M':
			dictionary = {'Male': 1, 'Female': 0}
			categories[curr_category] = dictionary
		elif entry['gender'] == 'F':
			dictionary = {'Male': 0, 'Female': 1}
			categories[curr_category] = dictionary
	else:
		dictionary = categories[curr_category]
		if entry['gender'] == 'M':
			dictionary['Male']+=1
			categories[curr_category] = dictionary
		elif entry['gender'] == 'F':
			dictionary['Female']+=1
			categories[curr_category] = dictionary

for entry in categories:
	males = categories[entry]['Male']
	females = categories[entry]['Female']
	print("For the Nobel Prize in ", entry, " the male/female ratio was ", round(males/females, 3),
		" (", males, " males and ", females, " females)", sep='')

print()
print('-'*70)
print()
