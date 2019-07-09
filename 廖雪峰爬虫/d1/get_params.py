import urllib.request
import urllib.parse
import string

def get_params():
    url = "http://www.baidu.com/s?wd="

    params = {
        "wd":"中文",
        "key":"zhang",
        "value":"san"
    }

    str_params = urllib.parse.urlencode(params)
    # print(str_params)
    #输出 wd=%E4%B8%AD%E6%96%87&key=zhang&value=san

    final_url = url + str_params

    #将带有中文的url转译成计算机可识别的url
    #解释器ascii没有汉子，url汉字转码
    end_url = urllib.parse.quote(final_url, safe=string.printable)

    response = urllib.request.urlopen(end_url)
    data = response.read().decode("utf-8")
    print(data)
get_params()