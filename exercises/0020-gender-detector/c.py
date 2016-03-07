from os.path import join, basename
from glob import glob
DATA_DIR = 'tempdata'

totals = {'M': set(), 'F': set()}

for f in glob(join(DATA_DIR, '*.txt')):
    year = basename(f)[3:7]
    if year >= "1950":
        for line in open(f, 'r'):
            name, gender, babies = line.split(',')
            totals[gender].add(name)


print("F:", str(len(totals['F'])).rjust(6),
      "M:", str(len(totals['M'])).rjust(6))

ratio = round(100 * len(totals['F']) / len(totals['M']))
print("F/M baby ratio:", ratio)