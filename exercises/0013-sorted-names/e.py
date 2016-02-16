import requests
import os
from os.path import join

directory = 'tempdata'
path = join(directory, 'ssa-babynames-nationwide-2014.txt')

def my_sort_function(item):
	return item['babies']

baby_list = []
total = 0
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0

names = {}
with open(path) as x:
    for line in x:
        name, sex, babies = line.strip().split(',')
        if names.get(name):
            names[name] += int(babies)
        else:
            names[name] = int(babies)
       	total+=int(babies)
for baby in names:
	current = {'name': baby, 'babies': names.get(baby)}
	baby_list.append(current)

baby_list = sorted(baby_list, key=my_sort_function, reverse=True)

for x in range(len(baby_list)):
	if x < 10:
		total1+=baby_list[x]['babies']
	elif x<100:
		total2+=baby_list[x]['babies']
	elif x<1000:
		total3+=baby_list[x]['babies']
	elif x<10000:
		total4+=baby_list[x]['babies']
	else:
		total5+=baby_list[x]['babies']
print("Names 1 to 10: " + str(round(total1*100/total, 1)))
print("Names 11 to 100: " + str(round(total2*100/total, 1)))
print("Names 101 to 1000: " + str(round(total3*100/total, 1)))
print("Names 1001 to 10000: " + str(round(total4*100/total, 1)))
print("Names 10001 to " + str(len(baby_list)) + ": " + str(round(total5*100/total, 1)))