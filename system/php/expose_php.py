# Author:w8ay
# Name:测试DEMO
'''
name: php expose_php模块开启
referer: http://blog.csdn.net/change518/article/details/39892449
author: Lucifer
description: 开启了expose_php模块。
'''


import HackRequests

def poc(arg, **kwargs):
    hack = HackRequests.hackRequests()

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/index.php?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000"
    vulnurl = arg + payload
    hh = hack.http(vulnurl, headers=headers)
    if r"XMLWriter" in hh.text() and r"phpinfo" in hh.text():
        result = {
            "name": "php expose_php",  # 插件名称
            "content": "开启了expose_php模块,referer: http://blog.csdn.net/change518/article/details/39892449",
            "url": vulnurl,  # 漏洞存在url
            "log": hh.log,
            "tag": "info_leak"  # 漏洞标签
        }
        return result




if __name__ == "__main__":
    pass