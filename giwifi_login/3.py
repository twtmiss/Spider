import requests

url = "http://login.gwifi.com.cn/cmps/admin.php/api/loginaction?round=123"
form_data = {
    'gw_id': 'GWIFI-qingdaogongxueyuan02',
'gw_address': '10.21.0.2',
'gw_port': '8060',
'url':' http://www.baidu.com',
'mac': '18:4F:32:F3:DA:5F',
'btype': 'pc',
'page_time': '1552201852',
'lastaccessurl': '',
'user_agent': '',
'devicemode': '',
'access_type': '0',
'station_sn': '000babf6a5f4',
'client_mac': '18:4F:32:F3:DA:5F',
'online_time': '125',
'logout_reason': '7',
'contact_phone': '400-038-5858',
'suggest_phone': '400-038-5858',
'station_cloud': 'login.gwifi.com.cn',
'acsign': 'd70286fd7f6afae7a6654e260638b8e5',
'sign': 'S%2FRGenBfMdrFUwrHBGpeqiD2aWQMG4%2BQzTdACmVsJk3bbXwS4qRqo1IAH5tjNFkKMkQT1B133X0shr2OdzpV2nk7eUtvn%2BiPre4JF6VvmnwwAKEF8o2HHzDLvD2CzNkKd68dtOqZzE2dFi07yx8TlJ5utvd350b5wNFFMjGd108A4SncbNABcL4RY00IA2U8AGxPUMIUVIKRl5ig3ylDdfCIxwE3dnNUbIDHPWUzMsitsNgRxW0Zu1as55jV1erC',
'name': '17852165622',
'password': '205209420'
}
header = """
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 744
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: PHPSESSID=ldu45joh4bf5qmcoihmf604au4
DNT: 1
Host: login.gwifi.com.cn
Origin: http://login.gwifi.com.cn
Referer: http://login.gwifi.com.cn/cmps/admin.php/api/login/?gw_address=10.21.0.2&gw_port=8060&gw_id=GWIFI-qingdaogongxueyuan02&ip=10.21.180.163&mac=18:4F:32:F3:DA:5F&url=http%3A//www.baidu.com%3Fua%3DMozilla&apmac=00:0b:ab:f6:a5:f4&ssid=
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
X-Requested-With: XMLHttpRequest

"""
#jsonData = request.POST(url)


#print(jsonData.text)

def st2object(s,s1=';',s2='='):
    li = s.split(s1)
    res={}
    for kv in li:
        li2 = kv.split(s2)
        if len(li2) > 1:
            res[li2[0]] = li2[1]

    return res
print(st2object(header,'\n',';'))

    http://10.21.0.2:8060/wifidog/get_auth_state?ip=10.21.180.163&mac=18:4F:32:F3:DA:5F&sign=aea53f35b6304ca9653f0a1fc2d59a29&callback=jQuery111006635127190595087_1552206923658&_=1552206923659