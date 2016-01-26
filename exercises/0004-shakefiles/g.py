import glob
import os

tragic_path = os.path.join("tempdata", "tragedies", "*")
tragic_filenames = glob.glob(tragic_path)

for tragedy in tragic_filenames:
	txtfile = open(tragedy, "r")
	mylist = txtfile.readlines()
	txtfile.close()
	total_lines = len(mylist)
	print(tragedy, "has", total_lines, "lines")
	starting_line_num = total_lines - 5
	for line_num in range(starting_line_num, total_lines):
		line = mylist[line_num]
		proper_line = str(line_num + 1) + ": " + line.strip()
		print(proper_line)