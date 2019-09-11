from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
#service = Service('/usr/bin/chromedriver')
#service.start()
#driver = webdriver.Remote(service.service_url)
driver = webdriver.Chrome()#      .Safari()

driver.get('https://music.163.com/#/song?id=488388942')
driver.switch_to_frame("g_iframe")
divNode = driver.find_element_by_xpath("//*[@class=\"itm\"]")
#print(divNode)
for node in divNode:
    print(node)