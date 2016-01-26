import os
fname = os.path.join("tempdata", "tragedies", "romeoandjuliet")
txtfile = open(fname, "r")
lines = 0
for x in range(4766-5):
	lines+=1
	txtfile.readline()

for line in txtfile:
	lines+=1
	the_line = str(lines) + ": " + line.strip()
	print(the_line)

txtfile.close()
