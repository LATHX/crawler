from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
opt = webdriver.ChromeOptions()
opt.headless = False
driver = webdriver.Chrome(options=opt)
driver.get('https://piao.ctrip.com/dest/u-_b1_b1_be_a9/s-tickets/')
def getData():
    itms = driver.find_elements_by_css_selector('.view-spot.clearfix')
    sale = '空'
    for itm in itms:
        s = itm.find_element_by_css_selector('.price-box>.price-num').text
        if s == '':
            s = '空'
        else:
            sale = itm.find_element_by_css_selector('.price-box>.sale').text
        print(itm.find_element_by_css_selector('.spot-info>h4>em').text,s,sale)

def nextPage():
    WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(by=By.LINK_TEXT, value='下一页')))
    button = driver.find_element_by_link_text('下一页').click()

i = 0
WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(by=By.CLASS_NAME, value='view-spot')))
for i in range(3):
    time.sleep(1)
    getData()
    nextPage()
    time.sleep(2)
    i = i +1

