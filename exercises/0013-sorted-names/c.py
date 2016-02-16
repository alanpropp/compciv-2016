from os.path import join

directory = 'tempdata'
path = join(directory, 'ssa-babynames-nationwide-2014.txt')

def my_sort_function(item):
	return (len(item['name']), item['babies'])

names = {}
with open(path) as x:
    for line in x:
        name, sex, babies = line.strip().split(',')
        if names.get(name):
            names[name] += int(babies)
        else:
            names[name] = int(babies)

top10 = []
for baby in names:
	current = {'name': baby, 'babies': names.get(baby)}
	if names.get(baby)>2000:
		top10.append(current)

top10 = sorted(top10, key=my_sort_function, reverse=True)

for x in range(10):
	print(top10[x]['name'].ljust(13), end="")
	string = str(top10[x]['babies'])
	print(string.rjust(12))