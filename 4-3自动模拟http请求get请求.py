#get请求实战--实现从横小说网信息自动搜索
import urllib.request,re
keyword="雪中悍刀行"
keyword=urllib.request.quote(keyword)
#page=&pageNo=2
for a in range(1,11):
    url="http://search.zongheng.com/s?keyword="+keyword+"&pageNo="+str(a)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    #print(len(data))
    #print(data)
    pat='<h2 class="tit"><a href="(.*?)" target="_blank" data-sa-d=\'{"page_module":"searchResPage","click_name":"book","book_id":"(.*?)"}\'>(.*?)</a></h2>'
    reg = "[A-Za-z0-9\!\%\[\]\,\。\<\=\"\/\>\s*]"
    rst=re.compile(pat).findall(data)
    for i in rst:
        print(re.sub(reg, '', i[2]))

    

