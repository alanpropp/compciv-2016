import os
import requests

website = "http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz"
resp = requests.get(website)
print("Downloading: " + website)
shakespeare = resp.text
mydirname = "tempdata"
myfilename = "matty.shakespeare.tar.gz"
myfullfilename = os.path.join(mydirname, myfilename)
outfile = open(myfullfilename, "w")
print("Writing file: " + myfullfilename)
outfile.write(shakespeare)
outfile.close()