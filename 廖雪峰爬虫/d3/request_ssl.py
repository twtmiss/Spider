import requests

url = "https://www.12306.cn"

header = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

#因为https 是有第三方CA证书认证的
#但是12306虽然是https，但是它不是CA证书，是自己颁布的证书
#解决方法：  告诉web忽略证书
#verify=False  忽略证书，但会报警告
'''
InsecureRequestWarning: Unverified HTTPS request is being made. 
Adding certificate verification is strongly advised. 
See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
'''
response = requests.get(url=url,headers=header,verify=False)
data = response.content.decode()

#with open(".\爬虫\廖雪峰爬虫\d3\\requests_ssl.html","w",encoding="utf-8") as f:
#    f.write(data)