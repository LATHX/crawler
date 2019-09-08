import requests
headers = {'Content-Type': 'application/x-www-form-urlencoded','Referer': 'https://music.163.com/album?id=35114938','Sec-Fetch-Mode': 'cors','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
url = 'http://music.163.com/api/v1/resource/comments/R_AL_3_35114938?limit=20&offset=4'
strhtml = requests.get(url,headers=headers)
print(strhtml.text)