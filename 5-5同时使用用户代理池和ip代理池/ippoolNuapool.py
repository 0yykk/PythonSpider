#一次提取十个
import urllib.request
import random
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
]

def ippool():
    allip=urllib.request.urlopen("http://tvp.daxiangdaili.com/ip/?tid=559126871522487&num=10&foreign=only").read().decode("utf-8","ignore")
    ippools=[]
    for thisip in allip:
        ippools.append(thisip)
        print(thisip)
    return ippools
def ip(ippools,uapools):
    thisip=random.choice(ippools)
    thisua=random.choice(uapools)
    print("当前浏览器为："+thisua)
    print("当前ip为："+thisip)
    headers=("User-Agent",thisua)
    proxy=urllib.request.ProxyHandler({"http":thisip})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)

pools=[]
for i in range(0,35):
    try:
        if(i%10==0):
            pools=ippool()
            print("获取代理池成功！")
            print(pools)
        ip(pools,uapools)    
        url="http://www.baidu.com"
        localpath="E:\\python爬虫\\5-5同时使用用户代理池和ip代理池\\bu.html"
        data=urllib.request.urlopen(url).read()
        res=data.decode("utf-8","ignore")
        print(len(res))
        fh=open(localpath,"w")
        fh.write(res)
        fh.close()
    except Exception as err:
        print(err)