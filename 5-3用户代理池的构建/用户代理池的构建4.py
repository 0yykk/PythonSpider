#一次提取十个
import urllib.request
import random
def ippools():
    allip=urllib.request.urlopen("http://tvp.daxiangdaili.com/ip/?tid=559126871522487&num=10&foreign=only").read().decode("utf-8","ignore")
    ippools=[]
    for thisip in allip:
        ippools.append(thisip.decode("utf-8","ignore"))
        print(thisip.decode("utf-8","ignore"))
    return ippools
def ip(ippools):
    thisip=random.choice(ippools)
    print(thisip)
    proxy=urllib.request.ProxyHandler({"http":thisip})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
x=0
pools=[]
for i in range(0,35):
    try:
        if(x%10==0):
            pools=ippools()
        ip(pools)    
        url="http://www.baidu.com"
        localpath=""
        data=urllib.request.urlopen(url).read()
        res=data.decode("utf-8","ignore")
        print(len(res))
        fh=open(localpath,"w")
        fh.write(res)
        fh.close()
        x+=1
    except Exception as err:
        print(err)
        x+=1