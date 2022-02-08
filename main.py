import requests

url = input("URL: ")
req = requests.get(url)
vidid = req.url.split("https://m.tiktok.com/v/")[1].split(".html")[0]

print(vidid)