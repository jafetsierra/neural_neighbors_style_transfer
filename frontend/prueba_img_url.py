import requests
url = "https://api.imgbb.com/1/upload"
payload = {}
files = {
    'image': ('S2.jpg', open('S2.jpg', 'rb')),
}
headers = {
  'key': '60a973fe05ef2eb8630752d9f05147a6',
  'expiration': '60'
}

response = requests.request("POST", url, params=headers, files=files)
print(response)