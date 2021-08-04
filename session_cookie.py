# import requests
# # 创建一个session对象，作用是会自动保存cookie
# session = requests.session()
# login_email = '账号'
# login_password = '密码'
# data = {
#     'login_email': login_email,
#     'login_password' : login_password
# }
# url = 'https://www.processon.com/login'
# # 用session发起post请求来获取登录后的cookie,cookie已经存在session中
# response = session.post(url=url, data=data)
# print(response.text)
#
# # 用session给个人主页发送请求，因为session中已经有cookie了
# index_url = 'https://www.processon.com/diagrams'
# index_page = session.get(url=index_url).text
# #
# print(index_page)
# 把cookie保存在本地，并判断用户是否已经登录

import requests
from http import cookiejar
# 创建一个session,作用是会自动保存
session = requests.session()
# 指定cookie保存的路径
session.cookies = cookiejar.LWPCookieJar(filename="cookies.txt")
try:
    session.cookies.load(ignore_discard=True)
except:
    print('cookie未能加载')


def login_save_cookie():
    # 登录并保存cookie到本地
    # return
    url = 'https://www.processon.com/login'
    login_email = '账号'
    login_password = '密码'
    data = {
        'login_email': login_email,
        'login-password': login_password,
    }
    # 使用session发起post请求来获取登陆后的cookie,cookie已经存在session中
    response = session.post(url=url, data=data)
    # 把cookie保存到文件中
    session.cookies.save()


def read_cookie():
    # 读取cookie进入登录页后的界面
    index_url = 'https://www.processon.com/diagrams'
    index_page = session.get(url=index_url).text
    print(index_page)


def login_y_n():
    """
    判断用户是否登录，我们这里使用的方法是：随便找一个登陆后页面的url,如果我们访问它时不发生重定向，我们就可以判断该用户应该登陆了
    :return:
    """
    url = 'https://www.processon.com/diagrams/new#template'
    response = session.get(url=url,allow_redirects=False)  # allow_redirects=Flase 不允许重定向到登录界面
    if response != 200:
        return False
    else:
        return True


read_cookie()



