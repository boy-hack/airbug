# Author:w8ay
# Name:目录浏览

import HackRequests
from urllib.parse import urlparse


def poc(arg, **kwargs):
    URL = arg
    netloc = urlparse(arg).netloc
    flag_list = [
        "<title>index of",
        "<title>directory listing for",
        "<title>{} - /".format(netloc)
    ]
    hack = HackRequests.hackRequests()
    url_list = [
        URL + "/css/", URL + "/js/", URL + "/img/", URL + "/images/", URL + "/upload/", URL + "/inc/"
    ]
    for u in url_list:
        hh = hack.http(u)
        if hh.status_code == 404:
            continue
        for i in flag_list:
            if i in hh.text():
                result = {
                    "name": "web目录浏览",  # 插件名称
                    "content": "通过此功能可获取web目录程序结构",  # 插件返回内容详情，会造成什么后果。
                    "url": u,  # 漏洞存在url
                    "log": hh.log,
                    "tag": "info_leak"  # 漏洞标签
                }
    return False
