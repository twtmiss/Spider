import urllib.request

def auth_neiwang():

    #用户名密码
    username = "admin"
    pwssword = "pwd"
    ip_url = "192.168.179.66"

    #创建密码管理器
    pwd_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm
    pwd_manager.add_password(None,ip_url,username,pwssword)

    #创建认证处理器
    auth_handler = urllib.request.HTTPBasicAuthHandler(pwd_manager)

    #创建opener
    opener = urllib.request.build_opener(auth_handler)

    response = opener.open(ip_url)
    


