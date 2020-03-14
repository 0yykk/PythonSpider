import urllib.request
#urlretrieve(网址，本地文件存储地址)直接下载网页到本地
urllib.request.urlretrieve("http://www.baidu.com","E:\\python爬虫\\baidu.html")

#urlcleanup()清除爬虫的缓存
#info()获取当前页面信息
file=urllib.request.urlopen("https://www.diyifanwen.com/zuowen/gaozhonghuatizuowen/")
print(file.info())
#getcode()输出状态码
print(file.getcode())
#geturl()获取当前网页的url
print(file.geturl())