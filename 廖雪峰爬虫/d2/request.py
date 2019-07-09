import requests
import urllib.request
import json


class RequestSpider(object):
    def __init__(self):

        url = "https://www.baidu.com"
        header = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

        #request 参数自动转译
        self.response = requests.get(url, headers = header)

    def run(self):
        data_run = self.response.content
        
        # 1. 获取请求头
        request_header = self.response.headers
        print("请求头：" + str(request_header))
        # 2. 获取响应头
        response_header = self.response.headers
        print("响应头" + str(response_header))
        # 3. 相应状态码
        code = self.response.status_code
        print("状态码" + str(code))
        # 4. 请求的cookie
        requests_cookie = self.response.request._cookies
        print("请求cookie:" + str(requests_cookie))
        #5. 响应的cookie
        response_cookie = self.response.cookies
        print("响应cookie:" + str(response_cookie))
        

    def res_data(self):
        response = requests.get(url)
        #content  属性 返回类型是bytes
        data_content = response.content
        print(data_content)
        #加上decode('utf-8)  返回类型 str
        data_utf = response.content.decode('utf-8')
        print(data_utf)
        #text属性 返回类型是文本str
        data_text = response.text
        print(type(data_text))

    def js(self):
        url = "http://api.github.com/user"
        header = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }
        response = requests.get(url,headers=header)

        data = response.content.decode('utf-8')
        #str -> dict
        data_dict = json.loads(data)
        print(data_dict)

        #json()自动将json字符串转换成str
        data = response.json()
        print(data)

RequestSpider().js()