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

for i in range(1,35):
    try:
        ua(uapools)
        url="http://qiushidabaike.com/index_"+str(i)+".html"
        data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
        pat='<dd class="content">(.*?)</dd>'
        reg = "[A-Za-z0-9\!\%\[\]\,\。\<\=\"\/\>]"
        rst=re.compile(pat,re.S).findall(data)
        for i in rst:
            print(re.sub(reg, '', i)+"\n")
            print("-----------")
    except Exception as err:
        print("异常")