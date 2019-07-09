from bs4 import BeautifulSoup
import requests


def reptile(label,url,class_id,find_id,class_id2,time_position,brief):

    li=[]

    header = {'User-Agent': 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
    }

    res = requests.get(url,headers = header)
    soup = BeautifulSoup(res.content.decode(res.encoding),"lxml")

    if label == 'news':
        s = soup.find_all(class_ = class_id)
    else:
        s = soup.find(class_ = class_id).find_all('p')
    #print(s)
    #print(label)
    for s1 in s:
  
        dic = {}
        #缩略图

        #文章标题
        if label == 'news':
            article_title = s1.find(find_id).find('a')['title']
        else:
            article_title = s1.find('a')['title']
        dic['article_title'] = article_title

        #作者
        article_author = s1.find(class_ =class_id2).find('a').string
        dic['article_author'] = article_author

        #时间
        article_publish_time = s1.find(class_ =class_id2).text.split()[time_position]
        dic['article_publish_time'] = article_publish_time

        #链接
        if label == 'news':
            article_link = 'http://www.infoq.com' + s1.find(find_id).find('a')['href']
        else:
            article_link = 'http://www.infoq.com' + s1.find('a')['href']
        dic['article_link'] = article_link


        #文章简介
        if label == 'news':
            for str in s1.find('p').stripped_strings:
                article_introduction = str
            dic['article_introduction'] = article_introduction
        
        #文章内容
        #待改内容格式
        #####################################################

        article_brief_url = article_link
        print(article_brief_url)
        article_brief_res = requests.get(article_brief_url,headers = header)
        article_brief_soup = BeautifulSoup(article_brief_res.content.decode(article_brief_res.encoding),"lxml")

        #s = soup.find_all(class_ = class_id)
        #print(brief)
        article_brief = article_brief_soup.find(class_ = brief).select('p')

        #####################################################
        dic['article_brief'] = ''#article_brief

        li.append(dic)
    
    return li
        
'''
    for k in s1.find_all('h3'):
        print(k)
        #print(k['class'])#查a标签的class属性
        #print(k['id'])#查a标签的id值
        #print(k['href'])#查a标签的href值
        print(k.text)#查a标签的string
        #tag.get('calss')，也可以达到这个效果
'''
'''
def time()




def sql()



'''

if __name__ == '__main__':
    list = [
        ['news','http://www.infoq.com/cn/news','news_type_block','h2','author',-1,'text_info'],
        ['java','http://www.infoq.com/cn/java/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk','this_is articles grid','p','about_general',-2,'text_info text_info_article'],
        ['Clojure','http://www.infoq.com/cn/clojure/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['Scala','http://www.infoq.com/cn/scala/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['.NET','http://www.infoq.com/cn/dotnet/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['移动','http://www.infoq.com/cn/mobile/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['Android','http://www.infoq.com/cn/android/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['iOS','http://www.infoq.com/cn/ios/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['HTML5','http://www.infoq.com/cn/html-5?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['JavaScript','http://www.infoq.com/cn/javascript/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['函数式编程','http://www.infoq.com/cn/fp/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['Web API','http://www.infoq.com/cn/webapi/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['架构','http://www.infoq.com/cn/architecture/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['企业架构','http://www.infoq.com/cn/enterprise-architecture/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['性能和可伸缩性','http://www.infoq.com/cn/performance-scalability/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['设计','http://www.infoq.com/cn/design/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['案例分析','http://www.infoq.com/cn/Case_Study/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['设计模式','http://www.infoq.com/cn/DesignPattern/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['安全','http://www.infoq.com/cn/Security/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['大数据','http://www.infoq.com/cn/bigdata/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['NoSQL','http://www.infoq.com/cn/nosql/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['数据库','http://www.infoq.com/cn/database/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['Agile','http://www.infoq.com/cn/agile/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['领导能力','http://www.infoq.com/cn/Leadership/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['团队协作','http://www.infoq.com/cn/team-collaboration/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['测试','http://www.infoq.com/cn/testing/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['用户体验','http://www.infoq.com/cn/ux/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['Scrum','http://www.infoq.com/cn/scrum/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['精益','http://www.infoq.com/cn/lean/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['持续交付','http://www.infoq.com/cn/continuous_delivery/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['自动化操作','http://www.infoq.com/cn/automation/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
        ['云计算','http://www.infoq.com/cn/cloud-computing/?utm_source=infoq&utm_medium=header_graybar&utm_campaign=topic_clk'],
    ]
    list2 = reptile(list[1][0],list[1][1],list[1][2],list[1][3],list[1][4],list[1][5],list[1][6])
    print('123')
    print(list2[0])