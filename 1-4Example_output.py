#小实例：输出乘法口诀
#end="" 代表不换行

#顺向输出
print("顺向输出")
for i in range(0,10):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
    print()

#逆向输出
print(" ")
print("逆向输出")
for i in range(9,0,-1):
    for j in range(i,0,-1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end=" ")
    print()

