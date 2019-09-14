import json
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
sql = 'select a.sale,lat,lng from ((select address,sale from qunar) a left join (select title,lat,lng from address) b on a.address = b.title) where lat != \"\"'
cur.execute(sql)
res = cur.fetchall()
points = []
for item in res:
    points.append({"lng":item[2],"lat":item[1],"count":item[0]})
str=json.dumps(points)
print(str)