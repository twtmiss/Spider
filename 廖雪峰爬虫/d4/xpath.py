import requests
from lxml import etree
#安装支持解析html和XML的解析库 lxml
#pip install lxml


url = "http://news.baidu.com"

header = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

data = requests.get(url,headers=header).content.decode()


#1. 转解析类型
xpath_data = etree.HTML(data)

#xpath语法 
# 下标从1开始   只能取平级关系的标签
# 1. 节点 /
# 2. 跨节点 //
# 3. 精确的标签  //a[@属性="属性值"]
# 4. 标签包裹的内容 text()
# 5. 属性  @href获取网址




#2.调用xpath的方法
result = xpath_data.xpath('/html/head/title/text')

result = xpath_data.xpath('//a/text()')

#获取指定标签内容， [@属性="属性值"]
result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=18"]/text()')
print(result)