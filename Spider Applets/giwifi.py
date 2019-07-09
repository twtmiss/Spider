import urllib.request
import urllib.parse
import gzip

fir_url = "http://login.gwifi.com.cn/cmps/admin.php/api/login/?"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "login.gwifi.com.cn",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

data = {
    "gw_address": "10.21.0.2",
    "gw_port": "8060",
    "gw_id": "GWIFI-qingdaogongxueyuan02",
    "ip": "10.21.180.163",
    "mac": "18:4F:32:F3:DA:5F",
    "url": "http://www.baidu.com",
    "ua": "Mozilla",
    "apmac": "",
    "ssid": ""
}

fir_parse_data = urllib.parse.urlencode(data).encode("utf-8")
request = urllib.request.Request(fir_url, headers= header, data= fir_parse_data)

response = urllib.request.urlopen(request)

datas = response.read()
datas_gzip = gzip.decompress(datas).decode("utf-8")
print(datas_gzip)

with open(".\爬虫\爬虫程序\giwifi.html","w") as f:
    f.write(datas_gzip)