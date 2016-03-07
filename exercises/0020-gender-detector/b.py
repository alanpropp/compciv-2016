from os.path import join, basename
from glob import glob
DATA_DIR = 'tempdata'
alltxtfiles_path = join(DATA_DIR, '*.txt')
alltxtfiles_names = glob(alltxtfiles_path)

post_names = []

for f in alltxtfiles_names:
	name = basename(f)
	year = name[3:7]
	if year >= "1950":
		post_names.append(f)

totals = {'M': 0, 'F': 0}

for f in post_names:
	current = open(f, "r")
	for line in current:
		name, gender, babies = line.split(',')
		totals[gender] += int(babies)

print("F:", str(totals['F']).rjust(6),
      "M:", str(totals['M']).rjust(6))

ratio = round(100 * totals['F'] / totals['M'])
print("F/M baby ratio:", ratio)