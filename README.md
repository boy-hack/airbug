# airbug
Airbug(空气洞),一个长期开放用于收集漏洞poc以及详情的学习平台,网络上此类平台似乎很少,就自己维护个吧,用于打发闲暇的无聊时光。  

所有POC文件按照一定格式编写，且支持python3.x，为了方便操作，Airbug平台所有网络访问需要使用[黑客们使用的http底层网络库 - hack-requests](https://github.com/boy-hack/hack-requests)引擎编写。  

- 因为使用了`hack-requests`，需要安装 `pip3 install HackRequests`

## Poc文件格式
POC内容用`poc(arg,**kwargs)`函数封装，不关注其他细节。
- 当poc验证成功时可返回文本或`Ture`或字典
- 若poc验证失败，返回`None`或`False`即可

## 参考
- [https://github.com/Lucifer1993/AngelSword](https://github.com/Lucifer1993/AngelSword)
- [https://github.com/vulhub/vulhub](https://github.com/vulhub/vulhub)