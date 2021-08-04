from selenium import webdriver
import json
# 写内核地址
browser = webdriver.Chrome(executable_path = r'内核地址')

def get_cookie():
    '''
    通过selenium获取cookie保存在文件中
    :return:
    '''
    url = 'https://www.processon.com/login'
    browser.get(url=url)
    browser.find_element_by_id('login_email').send_keys('账号')
    browser.find_element_by_id('login_password').send_keys('密码')
    browser.find_element_by_id('signin_btn').click()
    # 获取cookie,这里得到的是一个列表
    cookies_list = browser.get_cookies()
    browser.close()
    with open('cookies.txt', 'w') as fp:
        json.dump(cookies_list, fp)  ## 这里切记，如果我们要使用json.load读取数据，那么一定要使用json.dump来写入数据，
        # # 不能使用str(cookies)直接转为字符串进行保存，因为其存储格式不同。这样我们就将cookies保存在文件中了。

def read_cookie():
    """
    读取cookie,添加到browser中
    :return:
    """
    url = 'https://www.processon.com/diagrams'
    browser.get(url=url)
    with open('./cookies.txt', 'r') as fp:
        cookies_list = json.load(fp)
        for cookies in cookies_list:
            browser.add_cookie(cookies)
    browser.get(url)

read_cookie()