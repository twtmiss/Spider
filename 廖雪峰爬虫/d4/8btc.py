'''
爬取 8btc网站

'''

import requests
from lxml import etree
import re
import mysql.connector

class BtcSpider(object):
    
    def __init__(self):
        self.base_url = 'http://www.chainnode.com/forum/61-'
        self.header = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

    # 1. 发送请求
    def get_response(self,url):
        response = requests.get(url, headers=self.header)
        data = response.content.decode()
        #data = response.content  #以字节编码
        #print(data)
        return data
    
    
    # 2. 解析数据
    def parse_data(self, data):
        #使用xpath解析当前页面的所有新闻title和url
        # 1. 转类型
        x_data = etree.HTML(data,parser=etree.HTMLParser(encoding='utf-8'))
        #print(x_data)

        # 2. 根据xpath路径解析
        title1_list = x_data.xpath('//a[@class="link-primary font-bold bbt-block"]/text()')
        title2_list = x_data.xpath('//a[@class="link-dark-major font-bold bbt-block"]/text()')

        #将两个list合并
        title_list = title1_list + title2_list

        #消除标题左右两边的空格
        for i in range(len(title_list)):
            title_list[i] = title_list[i].strip()

        #将两个list合并
        url1_list = x_data.xpath('//a[@class="link-primary font-bold bbt-block"]/@href')
        url2_list = x_data.xpath('//a[@class="link-dark-major font-bold bbt-block"]/@href')
        url_list = url1_list + url2_list

        for i in range(len(url_list)):
            url_list[i] = 'http://www.chainnode.com' + url_list[i]

        #print(title_list)
        #print(url_list)

        data_list = []
        for index, title in enumerate(title_list):
            news = {}
            news['title'] = title
            news['url'] = url_list[index]
            data_list.append(news)
        #print(data_list)
        return data_list

    # 3. 保存数据
    def save_data(self, data,type):

        #如果以字节编码 
        #勿加   , encoding="utf-8"
        #否则会报错：binary mode doesn't take an encoding argument

        load = ".\爬虫\廖雪峰爬虫\d4\\8btc." + type

        with open(load,"w", encoding="utf-8") as f:
        #with open(".\爬虫\廖雪峰爬虫\d4\\8btc.html","wb") as f:

            
            f.write(data)

    def save_mysql(self,list):
        #连接数据库
        conn = mysql.connector.connect(host="localhost",user="root",passwd="admin",database="python_reptile")
        #创建游标
        mcursor = conn.cursor()
        
        sql_insert = 'insert into chainnode(title,url,typesof) values (%s, %s, %s)'
        val = []
        for i in list:
            val.append((i['title'],i['url'],re.findall('com/(.*)/',i['url'])[0]))
        
        #val格式为元组
        # val： [(),(),()]
        mcursor.executemany(sql_insert,val)
        conn.commit()

        try:
            print(mcursor.rowcount," 条数据插入成功")
        except:
            print("插入失败")
        
        

    # 4. 运行
    def run(self):
        # 1. 拼接url
        run_url = self.base_url+'1'

        # 2. 发送请求
        run_data = self.get_response(run_url)

        # 3. 解析数据
        data_list = self.parse_data(run_data)

        # 4. 保存数据

        #保存网页
        #self.save_data(run_data,'txt')
        
        #将数据保存至数据库
        self.save_mysql(data_list)


BtcSpider().run()