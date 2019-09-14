import pymysql
import urllib.parse
import requests
import json
db = pymysql.Connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'root',
    db = 'qunar',
    charset = 'utf8'
)
cur = db.cursor()

def get_geo_info(id,title):
    url = "http://api.map.baidu.com/geocoder/v2/?"
    param = {
        "output":"json",
        "ak":"tAwAffII9G0F8Gs4VRuXnuFmIdbOKCEu"
    }
    param.update({"address":title})
    data = urllib.parse.urlencode(param)
    url = url + data
    resp = requests.get(url)
    jsonText = json.loads(resp.text)
    print(jsonText)
    if jsonText["status"] == 0:
        lng = jsonText['result']['location']['lng']
        lat = jsonText['result']['location']['lat']
    else:
        lng = ''
        lat = ''
    print(lat,lng)
    updateSQL = "update address set lng = %s,lat = %s where id =%s"
    cur.execute(updateSQL,(lng,lat, id))
    db.commit()



sql = "select id,title from address"
res = cur.execute(sql)
res = cur.fetchall()

for item in res:
    print(item[1])
    get_geo_info(item[0], item[1])

