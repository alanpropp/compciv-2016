import shutil
import os
import requests
os.makedirs("tempdata", exist_ok = True)
zipurl = 'http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz'
resp = requests.get(zipurl)
zipdata = resp.content
zname = os.path.join("tempdata", "matty.shakespeare.tar.gz")
zfile = open(zname, "wb")
print("Unpacked " + zname + "into: tempdata")
zfile.write(zipdata)
zfile.close()
shutil.unpack_archive(zname, extract_dir = "tempdata")
