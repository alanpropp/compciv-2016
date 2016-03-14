from os.path import join, basename
import csv
DATA_DIR = 'tempdata'
WRANGLED_HEADERS = ['name', 'gender' , 'ratio' , 'females', 'males', 'total']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangledbabynames.csv')

START_YEAR = 1950
END_YEAR = 2014
years = list(range(START_YEAR, END_YEAR, 10))
years.append(END_YEAR)

overall_list = []
namesdict = {}

for year in years:
	filename = join(DATA_DIR, 'yob' + str(year) + '.txt')
	print("Parsing", filename)
	with open(filename, 'r') as thefile:
		for line in thefile:
			name, gender, count = line.split(',')
			if not namesdict.get(name): # need to initialize a new dict for the name
				namesdict[name] = {'M': 0, 'F': 0}
			namesdict[name][gender] += int(count)

#for each name, add to overall list
for name, counts in namesdict.items():
	current = {}
	current['name'] = name
	current['females'] = counts['F']
	current['males'] = counts['M']
	current['total'] = current['males'] + current['females']
	if current['females'] >= current['males']:
		current['gender'] = 'F'
		current['ratio'] = round(100*current['females']/current['total'])
	else:
		current['gender'] = 'M'
		current['ratio'] = round(100*current['males']/current['total'])
	overall_list.append(current)

#Sort function
def sort_function(dictionary):
	return (-dictionary['total'], dictionary['name'])
#Sort the list
overall_list = sorted(overall_list, key = sort_function)

#Create the CSV file
wfile = open(WRANGLED_DATA_FILENAME, 'w')
wcsv = csv.DictWriter(wfile, fieldnames=WRANGLED_HEADERS)
wcsv.writeheader()

#Write the file
for row in overall_list:
	wcsv.writerow(row)

wfile.close()

finalfile = open(WRANGLED_DATA_FILENAME, 'r')
lines = finalfile.readlines()[0:5]
for line in lines:
    print(line.strip())

