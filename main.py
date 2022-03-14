import requests

url = input("URL: ")
r = requests.get(url)
try:
    vidid = r.url.split("video/")[1].split("?")[0]
except:
    try:
        vidid = r.url.split("https://m.tiktok.com/v/")[1].split(".html")[0]
    except:
        print("An unknown error occured.")
print(vidid)
