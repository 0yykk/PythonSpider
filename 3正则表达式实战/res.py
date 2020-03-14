import re
string="xinqinghenhao"
#普通字符作为原子
pat="hao"
rst=re.search(pat,string)
print(rst)
#非打印字符作为原子
#\n \t
string='''baiduyun
weiyun
'''
pat="\n"
rst=re.search(pat,string)
print(rst)

#通用字符作为原子
#\w 字母数字下划线
#\W 除字母数字下划线
#\d 十进制数字
#\D 除十进制
#\s 空白字符
#\S 除空白字符
string='''xinqingyukuai213214aojids'''
pat="\d\d\d"
rst=re.search(pat,string)
print(rst)

#原子表
#[xyzi] [^xyzi]
string='''xinqingyukuai213214aojids'''
pat="xinq[xyzi]"
rst=re.search(pat,string)
print(rst)

#元字符
'''
.除换行外任意一个字符 pat="xin.i" 提取xinqing
^ 开始位置 pat="^xin.." 提取xinqi
$ 结束位置 pat="ji..$" 提取jids
* 0\1\多次 pat="xin.*" 提取xinqingyukuai213214aojids 因为.出现了多次
？ 0\1次
+ 1\多次
{n}恰好n次
{n,}至少n次
{n,m}至少n，至多m次
|模式选择符
（）模式单元
'''


#模式修正符
'''
I 匹配时候忽略大小写
M 多行匹配
L 本地化识别匹配
U unicode
S 让，匹配包括换行符*
'''
string="Python"
pat="pyt"
rst=re.search(pat,string,re.I)
print(rst)

#贪婪模式与懒惰模式
#贪婪模式 找到一个y以后继续往后找
string="pythony"
pat="p.*y"
rst=re.search(pat,string,re.I)
print(rst)

#懒惰模式 找到一个y以后停止，精准
string="pythony"
pat2="p.*?y"
rst=re.search(pat2,string,re.I)
print(rst)

#正则表达式函数
#1.match 2.search 3.全局匹配函数
#match只能从开头开始匹配 ，search什么地方都能开始匹配
string="pythony"
pat2="o.*?y"
rst=re.match(pat2,string,re.I)
print(rst)
#全局匹配函数 找到多个 re.compile(正则).findall(数据)
string="poythonypoiypnoy"
pat2="p.*?y"
rst=re.compile(pat2).findall(string)
print(rst)

#实例：匹配.com和.cn
string="<a href+'http://www.baidu.com'>百度首页</a>"
pat="[a-zA-Z]+://[\S]*[.com|.cn]"
rst=re.compile(pat).findall(string)
print(rst)
#实例：匹配电话号码
string="dsadsa021-1231412321sadsadsada0773-21321321sdadas"
pat3="\d{4}-\d{7}|\d{3}-\d{8}"
rst=re.compile(pat3).findall(string)
print(rst)