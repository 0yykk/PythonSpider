import urllib.request
ip="68.13.196.233:8080"
proxy=urllib.request.ProxyHandler({"http":ip})
opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
url="http://www.baidu.com"
localpath=""
data=urllib.request.urlopen(url).read()
res=data.decode("utf-8","ignore")
print(len(res))
fh=open(localpath,"w")
fh.write(res)
fh.close()