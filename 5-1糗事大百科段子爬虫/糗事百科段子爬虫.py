import urllib.request
import re
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(1,35):
    url="http://qiushidabaike.com/index_"+str(i)+".html"
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat='<dd class="content">(.*?)</dd>'
    reg = "[A-Za-z0-9\!\%\[\]\,\。\<\=\"\/\>]"
    rst=re.compile(pat,re.S).findall(data)
    for i in rst:
        print(re.sub(reg, '', i)+"\n")
        print("-----------")