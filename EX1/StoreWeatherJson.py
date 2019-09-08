import requests
import time
import pymongo
client = pymongo.MongoClient('localhost',27017)
book_weather = client['weather']
sheet_weather = book_weather['sheet_weather_3']
url = 'https://cdn.heweather.com/china-city-list.txt'
strhtml = requests.get(url)
strhtml.encoding = 'utf-8'
data = strhtml.text
data = data.replace('|','')
data = data.replace(' ','')
#print(data)
data1=data.split("\n")
print(len(data1))
for i in range(6):
    data1.remove(data1[0]) # Hi
i = 0
for item in data1:
    if(i==3):
        break;
    url = 'https://free-api.heweather.net/s6/weather/now?location=' + item[0:11] + '&key=dfbb883b35ae4a49a5ce6e7949536449'
    strhtml = requests.get(url)
    time.sleep(1)
    dic = strhtml.json()
    sheet_weather.insert_one(dic)
    i=i+1