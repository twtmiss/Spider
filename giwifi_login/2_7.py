#coding: utf-8
import urllib
from urllib import request
from urllib import parse
from urllib import response
import json
import sys
import time
import os

def get_rel_url():
    req=urllib.request.Request("http://172.21.1.1:8062/redirect")
    req.add_header('User-Agent','Mozilla/5.0(Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0')
    ipaddress=urllib.request.urlopen(req)
	#返回登陆页面的URl
    return ipaddress.geturl()

def qs(url):
	query = urllib.parse.urlparse(url).query
	rs_json = dict([(k,v[0]) for k,v in urllib.parse.parse_qs(query).items()])
	return rs_json

#初始化JSON
urljson = json.loads(json.dumps(qs(get_rel_url())))

#GiWiFi网关地址
def get_gw_address():
	return urljson['gw_address']

#本机MAC地址
def get_local_mac():
    return urljson['mac']

#本机IP地址
def get_local_ip():
    return urljson['ip']

#GiWiFi的AP MAC地址
def get_gw_mac():
    return urljson['apmac']

#GiWiFi的登陆网关端口
def get_gw_port():
    return urljson['gw_port']

#GiWiFi AP的SSID
def get_gw_ssid():
    return urljson['gw_id']

login_phone = "账号"
login_password = "密码"
json_data = {'gw_id':''+get_gw_ssid()+'',#GWIFI-qingdaogongxueyuan02
		'gw_address':''+get_gw_address()+'',#10.21.0.2
		'gw_port':''+get_gw_port()+'',#8060
		'url':'http://www.baidu.com',
		'ip':''+get_local_ip()+'',
		'mac':''+get_local_mac()+'',#18:4F:32:F3:DA:5F
		'apinfo':'',
		'btype':'pc',
		'PHPSESSID':'',
		'olduser':'0',
		'page_time':''+str(int(time.time()))+'',#1552054148
		'lastaccessurl':'',
		'user_agent':'',
		'devicemode':'',
		'access_type':'0',
		'station_sn':'2851320eb741',#000babf6a5f4
		'client_mac':''+get_gw_mac()+'',#18:4F:32:F3:DA:5F
		'online_time':'0',#12791
		'logout_reason':'7',#8
		'contact_phone':'400-038-5858',
		'suggest_phone':'400-038-5858',
		'station_cloud':'login.gwifi.com.cn',
		'acsign':'800ec48e04be9a2ea9804ce64648887e',
		#b4cbd6c4b971a43297b3c8148dd22757
		#每次改变
		'name':''+login_phone+'',
		'password':''+login_password+'',
		'service_type':'1'
		#'sign':'S%2FRGenBfMdrFUwrHBGpeqiD2aWQMG4%2BQzTdACmVsJk3bbXwS4qRqo1IAH5tjNFkKMkQT1B133X0shr2OdzpV2nk7eUtvn%2BiPre4JF6VvmnwwAKEF8o2HHzDLvD2CzNkKd68dtOqZzE2dFi07yx8TlJ5utvd350b5wNFFMjGd108A4SncbNABcL4RY00IA2U8AGxPUMIUVIKRl5ig3ylDdfCIxwE3dnNUbIDHPWUzMshCnB6ki7tWPZe1TS3oIxJo"
		}

def login():
    data = urllib.parse.urlencode(json_data).encode(encoding='UTF-8')

    #POST发送登陆数据
    req=urllib.request.Request('http://login.gwifi.com.cn/cmps/admin.php/api/loginaction?round=308')
    login_json=urllib.request.urlopen(req,data=data)
    #对返回的JSON数据进行解析
    auth_json=json.loads(login_json.read())
    auth_url=auth_json['info']
    #对解析到的地址继续发起GET请求并获取登陆状态
    end_login_status=urllib.request.urlopen(auth_url)
    return  end_login_status#返回登陆状态数据


def get_login_status():
	wifi_status_json = urllib.request.urlopen("http://"+get_gw_address()+":"+get_gw_port()+"/wifidog/get_auth_state?ip="+get_local_ip())
	status_json = json.loads(wifi_status_json.read())['data']
	auth_status = json.loads(status_json)['auth_state']
	if auth_status == 2:
		status = "GiWiFi online"
	else:
		status = "GiWiFi offline"
	return status


#获取登陆状态的JSON
get_json=json.loads(urllib.request.urlopen("http://"+get_gw_address()+":"+get_gw_port()+"/wifidog/get_auth_state?ip="+get_local_ip()).read())['data']


#解析登陆状态
end_status=json.loads(get_json)['auth_state']


#如果为2显示已经登陆
if end_status == 2:
	print('Login_Status:',get_login_status())


#循环检测是否在线
while 1 > 0:
	get_json=json.loads(urllib.request.urlopen("http://"+get_gw_address()+":"+get_gw_port()+"/wifidog/get_auth_state?ip="+get_local_ip()).read())['data']
	end_status=json.loads(get_json)['auth_state']
	#登陆状态不为2进行登陆
	if end_status != 2:
		print("Start login GiWifi ......")
		login()
		print("Login status"+get_login_status())
		#睡眠1s
		time.sleep(1)