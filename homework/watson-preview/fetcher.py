import requests
import os
PICS_DIR = 'pics'
os.makedirs(PICS_DIR, exist_ok = True)

url1 = "http://images.nypl.org/index.php?id=psnypl_the_4276&t=w&download=1&suffix=9b3ef73d-1c12-9bc9-e040-e00a18062530.001"
url2 = "https://farm2.staticflickr.com/1553/25183261081_24c2cfa470_z_d.jpg"
url3 = "https://farm2.staticflickr.com/1650/23610660263_fb3e97fd80_z_d.jpg"
url4 = "https://farm2.staticflickr.com/1491/23869646269_e05eea7ed8_z_d.jpg"
url5 = "https://upload.wikimedia.org/wikipedia/commons/8/8a/Kaiseradler_Aquila_heliaca_e_amk.jpg?download"

URLS = {url1, url2, url3, url4, url5}
URL_names = ["a.jpg", "b.jpg", "c.jpg", "d.jpg", "e.jpg"]
count = 0

for url in URLS:
    print("Downloading", url)
    resp = requests.get(url)
    fname = os.path.join(PICS_DIR, URL_names[count])
    count+=1
    print("Saving to", fname)
    with open(fname, 'wb') as w:
        w.write(resp.content)