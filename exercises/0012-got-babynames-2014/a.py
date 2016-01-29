import os
import requests

textfile = "ssa-babynames-nationwide-2014.txt"
myfile = os.path.join("tempdata", textfile)
outfile = open(myfile, "w")
resp = requests.get("http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt")
text = resp.text
outfile.write(text)
outfile.close
lines = text.splitlines()
print("There are",len(lines), "lines in", textfile)