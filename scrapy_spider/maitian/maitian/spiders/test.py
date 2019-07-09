'''
https://passport.weibo.com/visitor/visitor?
entry=miniblog
&a=enter
&url=https%3A%2F%2Fweibo.com%2F
&domain=.weibo.com
&ua=php-sso_sdk_client-0.6.28
&_rand=1555376362.4116
'''
import datetime
import json
import base64
from time import sleep
#import pymongo
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
#reload(sys)


WeiBoAccounts = [
{'username': 'javzx61369@game.weibo.com', 'password': 'esdo77127'},
{'username': 'v640e2@163.com', 'password': 'wy539067'},
{'username': 'd3fj3l@163.com', 'password': 'af730743'},
{'username': 'oia1xs@163.com', 'password': 'tw635958'},
]
#WeiBoAccounts = [{'username': '你的用户名', 'password': '你的密码'}]
cookies = []
#client = pymongo.MongoClient("192.168.98.5", 27017)
#db = client["Sina"]
#userAccount = db["userAccount"]
def get_cookie_from_weibo(username, password):
    driver = webdriver.PhantomJS()
    driver.get('https://weibo.cn')
    print(driver.title)
    
    assert "微博" in driver.title
    login_link = driver.find_element_by_link_text('登录')
    ActionChains(driver).move_to_element(login_link).click().perform()
    login_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginName"))
    )
    login_password = driver.find_element_by_id("loginPassword")
    login_name.send_keys(username)
    login_password.send_keys(password)
    login_button = driver.find_element_by_id("loginAction")
    login_button.click()    # 这里停留了10秒观察一下启动的Chrome是否登陆成功了，没有的化手动登陆进去
    sleep(10)
    cookie = driver.get_cookies()    #print driver.page_source
    print driver.current_url
    driver.close()    return cookie
def init_cookies():    for cookie in userAccount.find():
        cookies.append(cookie['cookie'])if __name__ == "__main__":    try:
        userAccount.drop()
    except Exception as e:
        pass    for account in WeiBoAccounts:
        cookie = get_cookie_from_weibo(account["username"], account["password"])
        userAccount.insert_one({"_id": account["username"], "cookie": cookie})
    init_cookies()
