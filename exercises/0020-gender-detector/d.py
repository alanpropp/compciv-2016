from os.path import join, basename
from glob import glob
DATA_DIR = 'tempdata'



for f in glob(join(DATA_DIR, '*.txt')):
	year = basename(f)[3:7]
	if year >= "1950":
		totals = {'M': set(), 'F': set()}
		for line in open(f, 'r'):
			name, gender, babies = line.split(',')
			totals[gender].add(name)
		print(year)
		print("F:", str(len(totals['F'])).rjust(6), "M:", str(len(totals['M'])).rjust(6))
		ratio = round(100 * len(totals['F']) / len(totals['M']))
		print("F/M baby ratio:", ratio)
