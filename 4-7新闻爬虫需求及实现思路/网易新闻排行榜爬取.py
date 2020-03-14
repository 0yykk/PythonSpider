import urllib.request
import re
newcount=0
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
#安装为全局
urllib.request.install_opener(opener)
#不安装全局
#data=opener.open(url).read()
url="https://news.163.com/rank/"
data=urllib.request.urlopen(url).read()
res=data.decode("gb18030")
#print(len(data))
'''
fh=open("E:\\python爬虫\\随便爬爬\\bu.html","wb")
fh.write(data)
fh.close()
'''
pat='<td class="red"><span>(.*?)</span><a href="(.*?)">(.*?)</a></td>'
allnew=re.compile(pat).findall(res)
if allnew:
    fh=open("E:\\python爬虫\\随便爬爬\\新闻列表.doc","w")
    for i in allnew:
        try:
            fh.write(i[2]+"    "+i[1]+"\n")
            newcount+=1
            localpath="E:\\python爬虫\\新闻爬虫需求及实现思路\\data\\"+str(newcount)+".html"
            newslink=str(i[1])
            urllib.request.urlretrieve(newslink,filename=localpath)
            print("第"+str(newcount)+"篇文章爬取成功")
        except Exception as err:
            print(err)
    fh.close()
else:
    print("爬取网页失败")