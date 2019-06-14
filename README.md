# airbug
Airbug(空气洞),一个长期开放用于收集漏洞poc仓库,可用于相关安全产品，亮点是能够在线加载poc并进行验证。

所有POC文件按照一定格式编写，且支持python3.x，为了方便操作，Airbug平台所有网络访问需要使用[黑客们使用的http底层网络库 - hack-requests](https://github.com/boy-hack/hack-requests)引擎编写。  

- 因为使用了`hack-requests`，需要安装 `pip3 install HackRequests`
### 目录结构
- cms 存放cms相关漏洞
- common 存放通用漏洞
- hardware 存放硬件漏洞
- system 存放一些系统的漏洞

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

### 参数传递

在调用poc函数时，有的poc需要传递多个参数，这里统一约定

| 序号 | 参数 | 解释        |
| ---- | ---- | ----------- |
| 1    | arg  | 传递一个url,格式:http\[s\]://xxx.xx 最后边没有`/` |
| 2    | ip   | 传递ip      |
| 3    | port | 传递端口    |

arg参数是必须的，如果有些情况只需要ip和端口，将arg置空，poc中读取ip，port即可，参考[system/iis/iis_webdav.py](system/iis/iis_webdav.py)

## 调用

airbug提供[API.json](API.json) 根据python的灵活性，可以在线调用，参考案例[w12scan](https://github.com/boy-hack/w12scan)

## 参考
- [https://github.com/Lucifer1993/AngelSword](https://github.com/Lucifer1993/AngelSword)
- [https://github.com/vulhub/vulhub](https://github.com/vulhub/vulhub)
- https://github.com/opensec-cn/kunpeng
