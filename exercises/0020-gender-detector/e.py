from os.path import join, basename
YEAR = 2014
DATA_DIR = 'tempdata'
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
print("Total:", len(all_names), "unique names for", all_babies, "babies")
print("    M:", len(male_names), "unique names for", male_babies, "babies")
print("    F:", len(female_names), "unique names for", female_babies, "babies")
