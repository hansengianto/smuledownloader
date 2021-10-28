import requests,re,urllib.request

url = "https://www.smule.com/sing-recording/1125341938_4193648178"
request = requests.get(f"https://sownloader.com/index.php?url={url}#support-sownloader").text
mp4 = re.findall("(?:url\=)(https:\/\/c-cl\.cdn\.smule\.com\/.+\.mp4)",request)

try:
	split_id = url.split("/")
	urllib.request.urlretrieve(mp4[0], split_id[4]+".mp4") 
	print("Success Download Video")
except Exception as e:
    print("Error Found : \n"+str(e))
