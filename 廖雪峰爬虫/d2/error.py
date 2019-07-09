import urllib.request



#   urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>
def urlerror():
    url = "http://www.afagubao.com"
    response = urllib.request.urlopen(url)

#   urllib.error.HTTPError: HTTP Error 404: Not Found
def httperror():
    url = "https://blog.csdn.net/weixin_36380516/article/details/737436"
    response = urllib.request.urlopen(url)


def f():
    url = "https://blog.csdn.net/weixin_36380516/article/details/7374366"

    try:
        response = urllib.request.urlopen(url)
    except urllib.request.HTTPError as error:
        print(error.code)       # 404
        print(error)            # HTTP Error 404: Not Found
    except urllib.request.URLError as error:
        print(error)            # 

f()