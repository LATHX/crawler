#!/Users/ljl/anaconda3/envs/tensorflow36/bin python
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
def isElementExist(element):
    flag=True
    try:
        driver.find_element_by_css_selector(element)
        return flag
    except:
        flag=False
        return flag

def getData():
    WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(by=By.CLASS_NAME, value='sight_item')))
    sightList = driver.find_elements_by_css_selector('.sight_item')
    for sight in sightList:
        sightHeader = sight.find_element_by_css_selector('.sight_item_detail.clrfix')
        title = sightHeader.find_element_by_css_selector('.sight_item_about').find_element_by_css_selector('.sight_item_caption>a').text
        sale = ''
        price = ''
        try:
            sale = sightHeader.find_element_by_css_selector('.sight_item_pop>table>tbody>tr>td>.hot_num').text
        except:
            sale = 0
        try:
            price = sightHeader.find_element_by_css_selector('.sight_item_pop>table>tbody>tr>td>.sight_item_price>em').text
        except:
            price = 0
        hot = sightHeader.find_element_by_css_selector('.sight_item_about>.sight_item_info>.clrfix>.sight_item_hot>.product_star_level>em').find_element_by_tag_name('span').get_attribute('style')
        address = sightHeader.find_element_by_css_selector('.sight_item_about>.sight_item_info>.address>span').text
        dt = datetime.date.today().strftime('%Y-%m-%d')
        if str(address).index('地址：')!=-1:
            address = str(address).replace('地址：','')
        if str(hot).index('width: ') !=-1 :
            hot = str(hot).replace('width: ','')
        if str(hot).index('%;') != -1:
            hot = str(hot).replace('%;', '')
        if hot.isnumeric() == False:
            hot = 0
        if str(price).isnumeric() == False:
            price = 0
        if str(sale).isnumeric() == False:
            sale = 0
        print(title,sale,price,hot,address)
        #cur.execute("insert into qunar (title,sale,price,hot,address,create_date) values (%s,%s,%s,%s,%s,%s)",(title,sale,price,hot,address,dt))
    #db.commit()
    time.sleep(2)

def nextPage(page,city):
    driver.get('http://piao.qunar.com/ticket/list.htm?keyword=%E7%83%AD%E9%97%A8%E6%99%AF%E7%82%B9&sort=pp&page='+str(page)+"&city="+city)

def check():
    sightList = driver.find_elements_by_css_selector('.sight_item')
    if sightList == None or len(sightList) == 0:
        return False
    return True
diming = ["基隆","淡水"]
for n in diming:
    page = 0
    for page in range(1000):#43
        print('当前第',(page+1),'页')
        nextPage(page+1,n)
        if check() == False:
            break;
        getData()
#driver.quit()