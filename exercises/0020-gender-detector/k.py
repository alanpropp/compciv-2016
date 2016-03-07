from os.path import join, basename
import csv
DATA_DIR = 'tempdata'
filename = join(DATA_DIR, 'wrangledbabynames.csv')



#Go through CSV file
def my_function(NAME):
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

name_list = ["Michael", "Kelly", "Kanye", "THOR", "casey", "Arya", "ZZZblahblah"]

F = 0
females = 0
M = 0
males = 0
NA = 0

#Enter the names required
for names in name_list:
	curr_dict = my_function(names)
	print(names, curr_dict['gender'], curr_dict['ratio'])
	if curr_dict['gender']=='NA':
		NA+=1
	else:
		males+=curr_dict['males']
		females+=curr_dict['females']
		if curr_dict['gender'] == 'M':
			M += 1
		elif curr_dict['gender'] == 'F':
			F += 1

print("Total:")
print("F:", F, "M:", M, "NA:", NA)
print("females:", females, "males:", males)



