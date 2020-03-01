print("hello world!")
'''print("hello world!")
#print("hello world!")'''

'''
数字、字符串、列表、元组、集合、字典
'''
a='abc'
a2="abc"
a3='''abc'''
print(a,a3,a2)
#列表：存储多个元素的东西，列表里面的元素是可以重新赋值的
b=[7,"cd",a,9]
print(b)
#元组：存储多个元素的东西，元组里面的元素不可以重新赋值
c=[a,2,4]
print(c)
#字典
#{键：值，键：值，键：值，。。。。}
#取值格式：字典名[“对应键名”]
d={"abc":7,"asd":8,"pgb":9,"cde":a}
print(d)

#集合
#去重
e=set("sadsadwqewq")
f=set("sadsawwqxxsf")
#e中有的f中没有的元素
g=e-f
print(g)

#缩进

#if
a=10
b=1
if(a>19):
    print(a)
    if(b<9):
        print(b)
elif(a>9 and a<=19):
    print("a>9 and a<=19")
#其他条件都不满足
else:
    print("abc")

#while语句
a=0
while(a<10):
    print("hello")
    a+=1

#for语句
#for:遍历列表
a=["aa","b","c","a"]
for i in a:
    print(i)

#for:常规循环
for i in range(0,10):
    print(i)
#for i in range(0,10)  0~9 print(i) 输出0~9
#continue、break
for i in a:
    if(i=="c"):
        break
    print(i)

