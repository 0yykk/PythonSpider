import urllib.request
import re
import random

uapools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
]

def ua(uapools):
    thisua=random.choice(uapools)
    print(thisua)
    headers=("User-Agent",thisua)
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    urllib.request.install_opener(opener)

keywrd="连衣裙"
kyw=urllib.request.quote(keywrd)
page=0
imgcount=1
#页数=2n-1
for i in range(1,19):
    try:
        if(i%2==0):
            page=i-1
        else:
            page=i
        ua(uapools)
        url="https://search.jd.com/Search?keyword="+kyw+"&enc=utf-8&suggest=1.def.0.V14--12s0,20s0,38s0,97s0&page="+str(page)
        data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
        pat='<img  data-presale="" data-sku="(.*?)" data-img="1" data-lazy-img="//(.*?)" class="err-product"'
        rst=re.compile(pat).findall(data)
        reg="\/n{1}\d"
        for a in rst:
            #print(a)
            localpath="E:\\python爬虫\\京东商品图片爬虫\\data\\"+str(a[0])+".jpg"
            thisimgurl="http://"+re.sub(reg, '/n0', a[1])
            urllib.request.urlretrieve(thisimgurl,filename=localpath)
            print("正在爬取第"+str(imgcount)+"张图片")
            imgcount+=1
        print("爬取结束总共抓取"+str(imgcount)+"张图片")
    except Exception as err:
        print(err)