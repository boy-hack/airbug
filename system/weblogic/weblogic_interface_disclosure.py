# Author:w8ay
# Name:测试DEMO

import HackRequests


def poc(arg, **kwargs):
    payload = "/bea_wls_deployment_internal/DeploymentService"
    vulnurl = arg + payload
    hack = HackRequests.hackRequests()

    try:
        hh = hack.http(vulnurl)
        if hh.status_code == 200:
            result = {
                "name": "weblogic 接口泄露",  # 插件名称
                "content": "存在weblogic 接口泄露漏洞",  # 插件返回内容详情，会造成什么后果。
                "url": vulnurl,  # 漏洞存在url
                "log": hh.log,
                "tag": "info_leak"  # 漏洞标签
            }
            return result

    except:
        pass


if __name__ == "__main__":
    pass