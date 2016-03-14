import requests
from os import makedirs
from os.path import join


SOURCE_URL = 'https://www.aggdata.com/download_sample.php?file=nobel.csv'
DATA_DIR = 'tempdata'
DATA_PATH = join(DATA_DIR, 'nobel.csv')
# make the directory
makedirs(DATA_DIR, exist_ok=True)

print("Downloading", SOURCE_URL)
resp = requests.get(SOURCE_URL)
# save it to disk
with open(DATA_PATH, 'wb') as f:
    # we use resp.content because it is BYTES
    f.write(resp.content)

