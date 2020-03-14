#URLerror出现的原因：
'''
1)连不上服务器
2）远程url不存在
3）无网络
4）除法HTTPError
'''
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://google.com")
except urllib.error.URLError as e:
    if hasattr(e,"reason"):
        print(e.reason)