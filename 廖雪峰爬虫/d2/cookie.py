'''
    www.yaozh.com

    1. 代码登录 登录成功 cookie（有效）
    2. 自动带着cookie去请求个人中心


'''



import urllib.request
from http import cookiejar
import urllib.parse

#### 
# 1. 代码登录
# 1.1 登录的网址
login_url = "https://www.yaozh.com/login"

# 1.2 登录的参数
login_from_data = {
    "username":"xiaomaoera12",
    "pwd":"lina081012",
    "formhash":"CBB5D23DB0",
    "backurl":"https%2F%2Fwww.yaozh.com"
}
## 参数需要转译(转码)；post请求的data要求是bytes
login_str = urllib.parse.urlencode(login_from_data).encode('utf-8')
# 1.3 发送登录请求
cook_jar = cookiejar.CookieJar()
#定义添加有cookie功能的处理器
cook_hanlder = urllib.request.HTTPCookieProcessor(cook_jar)
#根据处理器生成opener
opener = urllib.request.build_opener(cook_hanlder)

#添加请求头信息
header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

login_request = urllib.request.Request(login_url,headers=header,data=login_str)
#如果登录成功，cookiejar自动保存cookie
opener.open(login_request)


#### 2. 代码带着cookie去访问个人中心    
center_url = "https://www.yaozh.com/member/"
center_request = urllib.request.Request(center_url, headers=header)
response = opener.open(center_url)

# btes --> str
data = response.read().decode()

#data = response.read()
#print(data)

####windows系统需要指定编码为utf-8，因为默认编码格式为gbk
with open(".\爬虫\廖雪峰爬虫\d2\\yaozh.html","w",encoding="utf-8") as f:
    f.write(data)