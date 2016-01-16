import requests
resp = requests.get("https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-%E2%80%93-prepared-delivery-state-union-address")
resp_text = resp.text
print(resp_text.count('Applause'))
resp_text = resp_text.lower()
print(resp_text.count('applause'))
print(resp_text.count('<p>'))