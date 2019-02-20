# Author:w8ay
# Name:FTP 弱口令

import HackRequests
from urllib.parse import urlparse


def poc(arg, **kwargs):
    userlist = ["root","admin","www","ftp"]
    
    result = {
        "name": "web目录浏览",  # 插件名称
        "content": "通过此功能可获取web目录程序结构",  # 插件返回内容详情，会造成什么后果。
        "url": "",  # 漏洞存在url
        "log": "",
        "tag": "info_leak"  # 漏洞标签
    }
    return False
