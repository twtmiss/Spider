# pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests


# 1.转类型
# 默认bs4会调用系统中的lxml解析库 警告提示
# 主动设置bs4的解析库
#soup = BeautufulSoup(html, 'lxml')

# 2.格式化输出 补全
#result = soup.prettify()

'''
soup.head  取head标签
soup.p     取p标签

'''

class BtcSpider(object):
    def __init__(self):
        self.url = 'http://www.chainnode.com/forum/61-{}'
        self.header = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

    # 1. 发送请求
    def get_response(self, url):
        response = requests.get(url, headers=self.header)
        data = response.content.decode()
        return data

    # 2. 解析数据
    def parse_data(self, data, rule):

        # 1. 转类型
        soup = BeautifulSoup(data,'lxml')

        # 2.解析内容
        title_list = soup.select('.s')

        for title in title_list:
            print(title.get_text())

        pass

    # 3. 保存数据
    def save_data(self,data):
        with open(".\爬虫\廖雪峰爬虫\d4\\bs_btc.html","w",encoding="utf-8") as f:
            f.write(data)

    def start(self):
        #列表页的请求
        url = self.url.format(1)
        data = self.get_response(url)
        self.save_data(data)

BtcSpider().start()
