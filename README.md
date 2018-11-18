# airbug
Airbug(空气洞),一个长期开放用于收集漏洞poc以及详情的学习平台,网络上此类平台似乎很少,就自己维护个吧,用于打发闲暇的无聊时光。  

所有POC文件按照一定格式编写，且支持python3.x，为了方便操作，Airbug平台所有网络访问需要使用[黑客们使用的http底层网络库 - hack-requests](https://github.com/boy-hack/hack-requests)引擎编写。  

- 因为使用了`hack-requests`，需要安装 `pip3 install HackRequests`

## Poc文件格式
POC插件的格式设计崇尚简单易用，所有内容只需要用`poc(arg,**kwargs)`函数封装即可，不关注其他细节。
- 当poc验证成功时可返回文本或`Ture`或字典,为了返回详细信息，推荐使用字典返回形式
- 若poc验证失败，返回`None`或`False`即可  

```python
# Author:w8ay
# Name:测试DEMO

def poc(arg, **kwargs):
    result = {
        "name": "Demo插件",  # 插件名称
        "content": "如果这个插件能显示出来，就说明w12scan框架测试成功了",  # 插件返回内容详情，会造成什么后果。
        "url": arg,  # 漏洞存在url
        "log": {
            "send": "send",
            "response": "response"
        },
        "tag": "demo"  # 漏洞标签
    }
    return result


if __name__ == "__main__":
    pass

```

## 参考
- [https://github.com/Lucifer1993/AngelSword](https://github.com/Lucifer1993/AngelSword)
- [https://github.com/vulhub/vulhub](https://github.com/vulhub/vulhub)