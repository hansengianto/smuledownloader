import requests,re,urllib.request

##############################################
#Source : https://github.com/hansengianto
#Last Updated : 13 Feb 2022
##############################################

url = input("Please Input Your Smule URL To Download : ")
request = requests.get(f"https://sownloader.com/index.php?url={url}#support-sownloader").text
mp4 = re.findall("(?:url\=)(https:\/\/c-cl\.cdn\.smule\.com\/.+\.mp4)",request)
m4a = re.findall("(?:url\=)(https:\/\/c-cl\.cdn\.smule\.com\/.+m4a)",request)

choose = str(input("Choose Download video/audio : "))

if choose == "video":
	try:
		split_id = url.split("/")
		urllib.request.urlretrieve(mp4[0], split_id[4]+".mp4") 
		print("Success Download Video")
	except Exception as e:
		print("Error Found : \n"+str(e))

if choose == "audio":
	try:
		split_id = url.split("/")
		file_name = urllib.parse.unquote(split_id[4])
		urllib.request.urlretrieve(m4a[1], file_name+".m4a")
		print("Success Download Audio")
	except Exception as e:
		print("Error Found : \n"+str(e))

if choose != "video" and choose != "audio":
	print("Choose The Right One")
