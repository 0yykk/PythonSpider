#浏览器伪装
import urllib.request
url="http://blog.csdn.net"
#头文件格式header=("User-Agent",具体用户代理值)

headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36")
openner=urllib.request.build_opener()
openner.addheaders=[headers]
data=openner.open(url).read()
fh=open("E:\\python爬虫\\随便爬爬\\bu.html","wb")
fh.write(data)
fh.close()