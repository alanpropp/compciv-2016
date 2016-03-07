from os.path import join, basename
import json
DATA_DIR = 'tempdata'
filename = join(DATA_DIR, 'wrangledbabynames.json')



#Go through CSV file
def my_function(NAME):
	finalfile = open(filename, 'r')
	txt = finalfile.read()
	entries = json.loads(txt)
	my_dict = {'name': NAME,
	'gender': 'NA',
	'ratio': None,
	'males': None,
	'females': None,
	'total': 0
	}
	for entry in entries:
		if entry['name'].lower() == NAME.lower():
			my_dict['name'] = NAME
			my_dict['gender'] = entry['gender']
			my_dict['ratio'] = entry['ratio']
			my_dict['males'] = entry['males']
			my_dict['females'] = entry['females']
			my_dict['total'] = entry['total']
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



