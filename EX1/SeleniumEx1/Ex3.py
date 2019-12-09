from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time
opt = webdriver.ChromeOptions()
opt.headless = False
driver = webdriver.Chrome(executable_path='/Users/ljl/Documents/getData/EX1/SeleniumEx1/chromedriver',options=opt)
driver.get('https://music.163.com/#/song?id=488388942')
i = 0
WebDriverWait(driver, 30).until(EC.frame_to_be_available_and_switch_to_it('g_iframe'))
print('frame display')
def openWeb():
    print('------------',i,'---------------')
    WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(by=By.CLASS_NAME, value='itm')))
    print('itm display')
    itms = driver.find_elements_by_css_selector(".itm")
    if itms == None:
        print('None')
    else:
        for itm in itms:
            print(itm.find_element_by_class_name('cntwrap').find_element_by_css_selector('.cnt.f-brk').text)
        time.sleep(3)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)");
        #WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(by=By.LINK_TEXT, value='下一页')))
        button = driver.find_element_by_link_text('下一页').click()
try:
    for i in range(3):
        openWeb()
        time.sleep(3)
        i = i+1
except NameError:
    print(NameError)
finally:
    print('Finish')
    time.sleep(1)
    driver.quit()
