import urllib.request
import urllib.parse
postUrl="http://authserver.tjut.edu.cn/authserver/login"
postdata=urllib.parse.urlencode({
    "username":"20162070",
    "password":"1231451231",
}).encode("utf-8")
#进行post，就需要使用urllib.request下面的Request(真实地址，post数据)
req=urllib.request.Request(postUrl,postdata)
rst=urllib.request.urlopen(req).read().decode("utf-8")
print(rst)