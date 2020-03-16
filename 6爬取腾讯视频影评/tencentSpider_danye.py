#单页爬取20条
import urllib.request
import re

vid="vooy2m9hi5p1jqm"
reqnum="20"
cid="0"


url="https://video.coral.qq.com/filmreviewr/c/upcomment/"+vid+"?callback=_filmreviewrcupcomment"+vid+"&reqnum="+reqnum+"&source=132&commentid="+cid

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "Conten-Type":"application/javascript; charset=utf-8"
}

opener=urllib.request.build_opener()
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
opener.addheaders=headall
urllib.request.install_opener(opener)
#爬取当前评论页面
data=urllib.request.urlopen(url).read().decode("utf-8")
titlepat='"title":"(.*?)"'
commentpat='"content":"(.*?)",'
titleall=re.compile(titlepat,re.S).findall(data)
commentall=re.compile(commentpat,re.S).findall(data)
for i in range(0,len(titleall)):
    try:
        print("评论的标题是:"+eval('u"'+titleall[i]+'"'))
        print("评论的内容是:"+eval('u"'+commentall[i]+'"'))
        print("-------------------------------------------")
    except Exception as err:
        print(err)

