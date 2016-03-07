from os.path import join, basename
START_YEAR = 1950
END_YEAR = 2015
DATA_DIR = 'tempdata'
for YEAR in range(START_YEAR, END_YEAR, 5):
	filename = join(DATA_DIR, 'yob' + str(YEAR) + '.txt')
	male_names = {}
	female_names = {}
	all_names = {}
	male_babies = 0
	female_babies = 0
	all_babies = 0
	f = open(filename, 'r')
	for line in f:
		name, gender, babies = line.split(',')
		all_babies += int(babies)
		if(gender == 'M'):
			male_babies += int(babies)
			if not male_names.get(name):
				male_names[name] = int(babies)
			else:
				male_names[name] = int(male_names[name]) + int(babies)
		else:
			female_babies += int(babies)
			if not female_names.get(name):
				female_names[name] = int(babies)
			else:
				female_names[name] = int(female_names[name]) + int(babies)
		if not all_names.get(name):
			all_names[name] = int(babies)
		else:
			all_names[name] = int(all_names[name]) + int(babies)
	print(YEAR)
	print("Total:", int(round(all_babies/len(all_names), 0)),"babies per name")
	print("    M:", int(round(male_babies/len(male_names), 0)),"babies per name")
	print("    F:", int(round(female_babies/len(female_names), 0)),"babies per name")
