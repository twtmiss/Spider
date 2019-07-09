from selenium import webdriver

web = webdriver.Chrome()

def login_gwifi():
    web.get("http://10.21.0.2:8062/redirect")

    web.find_element_by_id("first_name").send_keys("17852165622")
    web.find_element_by_id("first_password").send_keys("205209420")
    web.find_element_by_id("first_button").click()
    #print(bro.page_source)
    #print(web.get_cookies())
    #web.close()

def fut():
    web.get("https://weibo.com/")
    print(web.page_source)


if __name__ ==  '__main__':
    fut()