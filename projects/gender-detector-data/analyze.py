import requests
from os import makedirs
from os.path import join
import csv

DATA_DIR = "tempdata"
DATA = "classified_data.csv"
DATA_PATH = join(DATA_DIR, DATA)
all_names = []

#Prints a division between 2 separate analyses (long dashed line)
def print_divider():
	print()
	print('-'*70)
	print()

print("\n\nData analysis on Nobel Prize winners since 1901\n")
print_divider()

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

#Total male/female ratio analysis, categories ratio analysis
print('Total male/female ratio for Nobel Prize winners over the years:')
total_male = 0
total_female = 0
total_NA = 0
categories = {}
countries = {}
for x in range(len(all_names)):
	entry = all_names[x]
	curr_category = entry['category']
	curr_country = entry['country']
	gender = entry['gender']
	if not categories.get(curr_category):
		if gender == 'M':
			dictionary = {'Male': 1, 'Female': 0}
			categories[curr_category] = dictionary
			total_male+=1
		elif entry['gender'] == 'F':
			dictionary = {'Male': 0, 'Female': 1}
			categories[curr_category] = dictionary
			total_female+=1
		elif entry['gender'] == 'NA':
			total_NA+=1
	else:
		dictionary = categories[curr_category]
		if entry['gender'] == 'M':
			dictionary['Male']+=1
			categories[curr_category] = dictionary
			total_male+=1
		elif entry['gender'] == 'F':
			dictionary['Female']+=1
			categories[curr_category] = dictionary
			total_female+=1
		elif entry['gender'] == 'NA':
			total_NA+=1

#Total male/female ratio analysis male/female ratio analysis (printing only)
print('Male/female ratio = ', round(total_male/total_female, 3), " (", total_male, 
	" males and ", total_female, " females)", sep = '')
print('There were also', total_NA, 'names for which we could not determine gender')
print_divider()


#Category-based male/female ratio analysis (printing only)
print('Category-based male/female ratio Nobel Prize winners:')
for entry in categories:
	males = categories[entry]['Male']
	females = categories[entry]['Female']
	print("For the Nobel Prize in ", entry, " the male/female ratio was ", round(males/females, 3),
		" (", males, " males and ", females, " females)", sep='')

print_divider()

#Decade-based male/female ratio analysis and printing
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
print_divider()

#Country-based male/female ratio analysis
for x in range(len(all_names)):
	entry = all_names[x]
	curr_country = entry['country']
	gender = entry['gender']
	if not countries.get(curr_country):
		if gender == 'M':
			dictionary = {'Male': 1, 'Female': 0}
			countries[curr_country] = dictionary
		elif entry['gender'] == 'F':
			dictionary = {'Male': 0, 'Female': 1}
			countries[curr_country] = dictionary
	else:
		dictionary = countries[curr_country]
		if entry['gender'] == 'M':
			dictionary['Male']+=1
			countries[curr_country] = dictionary
		elif entry['gender'] == 'F':
			dictionary['Female']+=1
			countries[curr_country] = dictionary

#Country-based male/female ratio analysis (printing only). Original
#plan was to find which countries had more female winners than male
#winners but (sadly) that number is depressingly tiny
print('Countries with female winners:')
print("The only countries with female winners were: ")
for entry in countries:
	males = countries[entry]['Male']
	females = countries[entry]['Female']
	if females != 0:
		print(entry, ": ", females, " female winners, ", round(100*females/(males+females), 3),
			" percent of winners in this country", sep = '')
print_divider()
