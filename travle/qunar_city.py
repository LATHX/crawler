from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import pymysql
opt = webdriver.ChromeOptions()
opt.headless = False
driver = webdriver.Chrome(options=opt)

db = pymysql.Connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'root',
    db = 'qunar',
    charset = 'utf8'
)

cur = db.cursor()

def getCityData():
    time.sleep(3)
    cityList = driver.find_elements_by_css_selector('.more_detail.clrfix')
    for item in cityList:
        dlList = item.find_elements_by_tag_name('dl')
        for dl in dlList:
            cityName = dl.find_element_by_tag_name('dd').get_attribute('data-value')
            sql = "insert into city (city_name) values (%s)"
            cur.execute(sql,(cityName))
            print(cityName)
            db.commit()

driver.get('http://piao.qunar.com/ticket/list.htm?keyword=%E7%83%AD%E9%97%A8%E6%99%AF%E7%82%B9&sort=pp')
getCityData()