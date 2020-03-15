#接口的调用适用于ip不稳定的状况
import urllib.request
def ip():
    thisip=urllib.request.urlopen("http://tvp.daxiangdaili.com/ip/?tid=559126871522487&num=1&foreign=only").read().decode("utf-8","ignore")
    print(thisip)
    proxy=urllib.request.ProxyHandler({"http":thisip})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

for i in range(0,5):
    try:
        ip()    #ip池直接通过网页api接口调用
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
