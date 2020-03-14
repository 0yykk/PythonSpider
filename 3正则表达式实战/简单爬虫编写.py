'''import urllib.request
data=urllib.request.urlopen("http://edu.csdn.net").read()'''
#提取课程的qq群
'''import urllib.request
import re
data1=urllib.request.urlopen("https://edu.csdn.net/huiyiCourse/detail/253").read().decode("utf-8","ignore")
#print(data1)
pat="<p>(\d*?)</p>"
rst=re.compile(pat).findall(data1)
print(rst)
'''

import urllib.request
import re

url="https://www.diyifanwen.com/zuowen/gaozhonghuatizuowen/"
response = urllib.request.urlopen(url)
html = response.read()
#print(html)
res=html.decode("gb2312")
#print(res)
pat1='<li><a  target="_blank" href="//(.*?)" title="(.*?)">(.*?)</a></li>'
rst=re.compile(pat1).findall(res)
fh=open("E:\\python爬虫\\3正则表达式实战\\爬取的作文地址.txt","w")
for i in rst:
    print(i[1]+"    链接："+i[0])
    fh.write(i[1]+"    "+i[0]+"\n")
fh.close()



