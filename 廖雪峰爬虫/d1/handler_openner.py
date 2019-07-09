import urllib.request

def handler_openner():
    #系统的urlopen并没有添加代理的功能，所以需要我们自定义这个功能
    #安全套接层 ssl第三方的CA数字证书
    #http 80端口  https 443端口
    #urlopen为什么可以请求数据  handler处理器
    #自己的opener请求数据

    #urllib.request.urlopen()

    url = "https://blog.csdn.net/shuai_wy/article/details/79024790"

    #创建自己的处理器
    handler = urllib.request.HTTPHandler()

    #创建自己的opener
    opener = urllib.request.build_opener(handler)

    #用自己创建的opener调用open方法请求数据
    response = opener.open(url)
    data = response.read()

    print(data)

def create_proxy_handler():

    url = "https://blog.csdn.net/shuai_wy/article/details/79024790"

    #添加代理
    '''
    proxy = {
        #免费代理ip写法
        "http":"http://120.77.249.46:8080"
        #付费代理
        #"http":"账户名":密码@ip地址
    }
    '''

    proxy_list = [
        {"http":"120.77.249.46:8080"},
        {"http":"106.75.226.36:808"},
        {"http":"61.135.217.7:80"},
        {"http":"125.70.13.77:8080"},
        {"http":"118.190.95.35:9001"}
    ]

    for i in proxy_list:
        print(i)
        #利用遍历的ip创建处理器
        #代理处理器
        proxy_handler = urllib.request.ProxyHandler(i)

        #创建自己的opener
        opener = urllib.request.build_opener(proxy_handler)
        
        #拿着代理ip去发送请求
        #如果某一个ip出现问题无法使用，抛出异常后使用下一个ip地址
        try:
            data = opener.open(url,timeout = 2).read()
            #print(data)
        except Exception as e:
            print(e)

def money_proxy_use():
    #1. 代理ip
    money_proxy = {"http":"username:pwd@192.168.12.11:8080"}

    #2. 代理的处理器
    proxy_handler = urllib.request.ProxyHandler(money_proxy)

    #3. 通过处理器创建opener
    opener = urllib.request.build_opener(proxy_handler)

    #4. open发送请求
    opener.open("http://www.naidu.com")


    ######第二种方式
    use_name = "username"
    pwd = "qwer"
    proxy_ip = "123.123.12.123:8080"

    #创建密码管理器，添加用户名和密码
    pwssword_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    #uri 定位 uri > url
    #url 资源定位符
    pwssword_manager.add_password(None,proxy_ip,use_name,pwd)
    #创建可以验证代理ip的处理器
    handle_auth_proxy = urllib.request.ProxyBasicAuthHandler(pwssword_manager)
    # 根据处理器创建opener
    opener_auth = urllib.request.build_opener(handle_auth_proxy)
    #发送请求
    response = opener_auth.open("http://www.baidu.com")

create_proxy_handler()
#handler_openner()