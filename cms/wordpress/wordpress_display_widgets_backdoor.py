# Author:w8ay
# Name:测试DEMO
'''
name: wordpress display-widgets插件后门漏洞
referer: http://www.nsfocus.com.cn/upload/contents/2017/09/20170915174457_73771.pdf
author: Lucifer
description: wordpress display-widgets Version 2.6.1——Version 2.6.3.1 geolocation.php存在后门。
'''

import HackRequests


def poc(arg, **kwargs):
    payload = "/wp-content/plugins/display-widgets/geolocation.php"

    vulnurl = arg + payload
    try:
        hack = HackRequests.hackRequests()
        hh = hack.http(vulnurl)

        if hh.status_code == 200:
            result = {
                "name": "wordpress display-widgets插件后门",  # 插件名称
                "content": "存在wordpress display-widgets插件后门漏洞",  # 插件返回内容详情，会造成什么后果。
                "url": vulnurl,  # 漏洞存在url
                "log": hh.log,
                "tag": "backdoor"  # 漏洞标签
            }
            return result
    except:
        pass


if __name__ == "__main__":
    pass