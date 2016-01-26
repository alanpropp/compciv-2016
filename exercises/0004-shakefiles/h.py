import os
import glob
import requests

all_line_count = 0
all_nonblank_line_count = 0

filepattern = os.path.join("tempdata", "**", "*")
filenames = glob.glob(filepattern)
for fname in filenames:
	txtfile = open(fname, "r")
	total_line_count = 0
	nonblank_line_count = 0
	for line in txtfile:
		total_line_count+=1
		if line.strip() is not "":
			nonblank_line_count+=1
	txtfile.close()
	print(fname, "has", nonblank_line_count, 
		"non-blank lines out of", total_line_count, "total lines")
	all_line_count+=total_line_count
	all_nonblank_line_count+=nonblank_line_count
print("All together, Shakespeare's", len(filenames),
	"text files have:", all_nonblank_line_count, 
	"non-blank lines out of", all_line_count, "total lines")
