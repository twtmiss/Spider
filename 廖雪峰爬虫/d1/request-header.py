import urllib.request
import random


def load_baidu():
    url = "http://www.baidu.com"

    #添加请求头信息
    header = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }

    
    #创建请求对象
    request = urllib.request.Request(url, headers=header)

    #动态添加header信息
    #request = urllib.request.Request(url)

    user_agent_list = [
        "",
        "",
        "",
        ""
    ]
    #每次从user_agent_list里随机获取一个User-Agent,添加到请求头里
    #random_user_agent = random.choice(user_agent_list)
    #request.add_header("User-agent",random_user_agent)


    #request.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")
    
    response = urllib.request.urlopen(request)

    data = response.read().decode("utf-8")

    # 响应头
    #print(response.headers)

    #获取请求头的信息(所有信息)
    request_headers = request.headers
    #print(request_headers)

    #获取请求头里的指定信息(首字母大写 其余字母小写)
    request_headers1 = request.get_header("User-agent")
    print(request_headers1)
    #with open(".\爬虫\廖雪峰爬虫\d1\\baidu.html", "w") as f:
    #   f.write(data)

load_baidu()
