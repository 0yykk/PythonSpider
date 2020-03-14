import urllib.request
for i in range(0,100):
    try:
        file=urllib.request.urlopen("https://cn.bing.com/",timeout=0.5)
        print(len(file.read().decode("utf-8")))
    except Exception as err:
        print("异常："+str(err))