import requests
for i in range(1, 8):
	website = None
	if i == 1:
		website = requests.get("https://www.whitehouse.gov/the-press-office/remarks-president-barack-obama-address-joint-session-congress")
	if i == 2:
		website = requests.get("https://www.whitehouse.gov/the-press-office/remarks-president-state-union-address")
	if i == 3:
		website = requests.get("https://www.whitehouse.gov/the-press-office/2011/01/25/remarks-president-state-union-address")
	if i == 4:
		website = requests.get("https://www.whitehouse.gov/the-press-office/2013/02/12/remarks-president-state-union-address")
	if i == 5:
		website = requests.get("https://www.whitehouse.gov/the-press-office/2014/01/28/president-barack-obamas-state-union-address")
	if i == 6:
		website = requests.get("https://www.whitehouse.gov/the-press-office/2015/01/20/remarks-president-state-union-address-january-20-2015")
	if i == 7:
		website = requests.get("https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-%E2%80%93-prepared-delivery-state-union-address")
	print(website.url)
	print(len(website.text))
	website = website.text.lower()
	print(website.count('applause'))
