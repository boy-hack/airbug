#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: dedecms版本探测
referer: unknow
author: Lucifer
'''
import HackRequests
import re


def check_ver(arg):
    ver_histroy = {'20080307': 'v3 or v4 or v5',
                   '20080324': 'v5 above',
                   '20080807': '5.1 or 5.2',
                   '20081009': 'v5.1sp',
                   '20081218': '5.1sp',
                   '20090810': '5.5',
                   '20090912': '5.5',
                   '20100803': '5.6',
                   '20101021': '5.3',
                   '20111111': 'v5.7 or v5.6 or v5.5',
                   '20111205': '5.7.18',
                   '20111209': '5.6',
                   '20120430': '5.7SP or 5.7 or 5.6',
                   '20120621': '5.7SP1 or 5.7 or 5.6',
                   '20120709': '5.6',
                   '20121030': '5.7SP1 or 5.7',
                   '20121107': '5.7',
                   '20130608': 'V5.6-Final',
                   '20130922': 'V5.7SP1'}
    ver_list = sorted(list(ver_histroy.keys()))
    ver_list.append(arg)
    sorted_ver_list = sorted(ver_list)
    return ver_histroy[ver_list[sorted_ver_list.index(arg) - 1]]


def poc(arg, **kwargs):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/data/admin/ver.txt"
    vulnurl = arg + payload
    hh = HackRequests.hackRequests()
    try:
        r = hh.http(vulnurl, headers=headers)

        if r.status_code == 200 and len(r.text()) < 500:
            m = re.search("^(\d+)$", r.text())
            version = "Not found"
            if m:
                version = check_ver(m.group(1))
            msg = "探测到dedecms版本:{} version:{}".format(r.text(), version)
            result = {
                "name": "dedecms version_leak",  # 插件名称
                # 插件返回内容详情，会造成什么后果。
                "content": msg,
                "url": vulnurl,  # 漏洞存在uzrl
                "log": r.log,
                "tag": "info_leak"  # 漏洞标签
            }
            return result

    except:
        return False
