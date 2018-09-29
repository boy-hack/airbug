# Author:w8ay
# Name:测试DEMO
'''
name: discuz X3 focus.swf flashxss漏洞
referer: unknown
author: Lucifer
description: 文件中focus.swf存在flashxss。
'''
import hashlib
import HackRequests


def poc(arg, **kwargs):
    flash_md5 = "c16a7c6143f098472e52dd13de85527f"
    payload = "/static/image/common/focus.swf"
    vulnurl = arg + payload
    hack = HackRequests.hackRequests()
    hh = hack.http(vulnurl)
    if hh.status_code != 200:
        return False
    data = hh.content()
    md5_value = hashlib.md5(data).hexdigest()

    if md5_value == flash_md5:
        result = {
            "name": "DZ X3 flash xss",  # 插件名称
            "content": "存在discuz X3 focus.swf flashxss漏洞...",  # 插件返回内容详情，会造成什么后果。
            "url": vulnurl,  # 漏洞存在url
            "log": hh.log,
            "tag": "flash_xss"  # 漏洞标签
        }
        return result


if __name__ == "__main__":
    pass