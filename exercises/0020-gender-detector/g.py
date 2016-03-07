from os.path import join, basename
import csv
DATA_DIR = 'tempdata'
YEAR = 2014
thefilename = join(DATA_DIR, 'yob' + str(YEAR) + '.txt')

WRANGLED_HEADERS = ['year', 'name', 'gender' , 'ratio' , 'females', 'males', 'total']
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')

overall_list = []
namesdict = {}

#Fill up namesdict with all the names
with open(thefilename, 'r') as thefile:
    for line in thefile:
        name, gender, count = line.split(',')
        if not namesdict.get(name): # need to initialize a new dict for the name
            namesdict[name] = {'M': 0, 'F': 0}
        namesdict[name][gender] += int(count)

#for each name, add to overall list
for name, counts in namesdict.items():
	current = {}
	current['year'] = YEAR
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
