# Author:w8ay
# Name:Metinfo版本识别
import HackRequests

def getMiddle(src,a,b):
    try:
        aa = src.index(a)
        bb = src.index(b,aa)
    except ValueError:
        return ""
    return src[aa + len(a):bb]

def poc(arg, **kwargs):
    hh = HackRequests.http(arg)
    if hh.status_code != 200:
        return False
    version = getMiddle(hh.text(),'<meta name="generator" content="','" />')
    if version == "":
        return False

    result = {
        "name": "Metinfo版本识别",  # 插件名称
        "content": "version:{}".format(version),  # 插件返回内容详情，会造成什么后果。
        "url": arg,  # 漏洞存在url
        "log": hh.log,
        "tag": "info_leak"  # 漏洞标签
    }
    return result


if __name__ == "__main__":
    pass