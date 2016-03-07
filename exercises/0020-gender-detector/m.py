from os.path import join, basename
import csv
import json
DATA_DIR = 'tempdata'
filename = join(DATA_DIR, 'wrangledbabynames.csv')
json_filename = join(DATA_DIR, 'wrangledbabynames.json')

nameslist = []

experiment = 0
with open(filename, 'r') as thefile:
	reader = csv.reader(thefile)
	next(reader, None)
	for line in reader:
		current = {}
		current['name'] = line[0]
		current['gender'] = line[1]
		current['ratio'] = int(line[2])
		current['females'] = int(line[3])
		current['males'] = int(line[4])
		current['total'] = int(line[5])
		nameslist.append(current)
	thefile.close()

wfile = open(json_filename, 'w')
wfile.write(json.dumps(nameslist, indent = 2))
csv_length = 0
json_length = 0
with open(filename, 'r') as thefile:
	data = thefile.read()
	csv_length = len(data)
	print("CSV has", csv_length, "characters")
	thefile.close()

with open(json_filename, 'r') as thefile:
	data = thefile.read()
	json_length = len(data)
	print("JSON has", json_length, "characters")
	thefile.close()

print("JSON requires", round((json_length/csv_length)-1, 1), 
	"times more text characters than CSV")


