import urllib.request
import requests


def load_baidu():
    url = "http://weibo.cn/"
    mobile_url = "https://m.weibo.cn/detail/4357361299343563"
    m_url = "https://m.weibo.cn/?jumpfrom=weibocom"
    #添加请求头信息
    header = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "weibo.com"
    
    
    }
    mobile_headers = {
        "Host": "m.weibo.cn",
        "Upgrade-Insecure-Requests": 1,
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "keep-alive",
        "Cookie": "MLOGIN=0; _T_WM=7b0a246c23875f47d79c39f2cb3133eb; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803%26uicode%3D10000011%26fid%3D102803",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "Trailers"
        }
    m_headers ={
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"

    }
    

    
    #创建请求对象
    #request = urllib.request.Request(url, headers=header)
    #response = urllib.request.urlopen(request)
    #data = response.read()#.decode("utf-8")
    request = requests.get(url=m_url,headers=m_headers)
    data = request.content.decode()
    print(data)

    with open(".\爬虫\爬虫程序\weibo.html", "w",encoding="utf-8") as f:
       f.write(str(data))

load_baidu()
