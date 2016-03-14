from os.path import join, basename
import csv
DATA_DIR = 'tempdata'
filename = join(DATA_DIR, 'wrangledbabynames.csv')



#Go through CSV file
def detect_gender(NAME):
	finalfile = open(filename, 'r')
	my_dict = {'name': NAME,
	'gender': 'NA',
	'ratio': None,
	'males': None,
	'females': None,
	'total': 0
	}
	reader = csv.reader(finalfile)
	next(reader, None)
	for line in reader:
		if line[0].lower() == NAME.lower():
			my_dict['name'] = NAME
			my_dict['gender'] = line[1]
			my_dict['ratio'] = int(line[2])
			my_dict['males'] = int(line[4])
			my_dict['females'] = int(line[3])
			my_dict['total'] = int(line[5])
			finalfile.close()
			return my_dict
	finalfile.close()
	return my_dict

