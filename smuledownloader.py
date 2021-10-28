import requests,re,urllib.request

##############################################
#Source : https://github.com/hansengianto
#Date : 28 Oct 2021
##############################################

url = input("Input Smule Video URL : ")
request = requests.get(f"https://sownloader.com/index.php?url={url}#support-sownloader").text
mp4 = re.findall("(?:url\=)(https:\/\/c-cl\.cdn\.smule\.com\/.+\.mp4)",request)

try:
	split_id = url.split("/")
	urllib.request.urlretrieve(mp4[0], split_id[4]+".mp4") 
	print("Success Download Video")
except Exception as e:
    print("Error Found : \n"+str(e))
