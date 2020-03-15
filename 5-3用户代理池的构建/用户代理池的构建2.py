import random
import urllib.request
ippools=[
    "112.247.66.254:9999",
    "112.247.100.200:9999",
    "112.247.5.22:9999",
]

def ip(ippools):
    thisip=random.choice(ippools)
    print(thisip)
    proxy=urllib.request.ProxyHandler({"http":thisip})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

for i in range(0,5):
    try:
        ip(ippools)
        url="http://www.baidu.com"
        localpath=""
        data=urllib.request.urlopen(url).read()
        res=data.decode("utf-8","ignore")
        print(len(res))
        fh=open(localpath,"w")
        fh.write(res)
        fh.close()
    except Exception as err:
        print(err)