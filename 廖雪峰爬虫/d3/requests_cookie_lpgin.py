import requests

yaozh_member_url = "https://www.yaozh.com/member/"

header = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
        }

#requests.session 可以自动保存cookies 等于cookiesJar
session = requests.session()

#1. 代码登录
yaozh_login_url = "https://www.yaozh.com/login"
login_form_data = {
    "username":"xiaomaoera12",
    "pwd":"lina081012",
    "formhash":"CBB5D23DB0",
    "backurl":"https%2F%2Fwww.yaozh.com"
}

login_response = session.post(url=yaozh_login_url,data=login_form_data, headers=header)

#2. 登录成功之后 带着有效的cookies访问请求目标数据

data = session.get(url=yaozh_member_url, headers=header).content.decode()

with open(".\爬虫\廖雪峰爬虫\d3\\cookie_login.html", "w", encoding="utf-8") as f:
    f.write()

