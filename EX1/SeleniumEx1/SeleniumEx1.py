from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#service = Service('/usr/bin/chromedriver')
#service.start()
#driver = webdriver.Remote(service.service_url)
driver = webdriver.Safari()#.Chrome()
driver.get('https://sites.google.com/a/chromium.org/chromedriver/home')