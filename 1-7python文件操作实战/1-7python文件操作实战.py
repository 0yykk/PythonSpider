#文件的操作
#打开
#open(文件地址，操作形式)    w:写  r:读取 b:二进制  a:追加内容
fh=open("E:/python爬虫/1-7python文件操作实战/测试文本.txt","r",encoding="UTF-8")
data=fh.read()
#print(data)
#读取一行readline()
line=fh.readline()
fh.close()
#print(line)

#文件的写入
data="随便写写！"
fh2=open("E:/python爬虫/1-7python文件操作实战/测试文本1.txt","w",encoding="UTF-8")
fh2.write(data)
fh2.write("随便画画！")
fh2.close()
#close()之后才会进行保存
#a+追加，运行一次写入一段文本 
fh3=open("E:/python爬虫/1-7python文件操作实战/测试文本3.txt","a+",encoding="UTF-8")
fh3.write(data)
fh3.close()
#关闭文件 close()