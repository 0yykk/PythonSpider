#异常处理
#try catch
try:
    for i in range(0,10):
        print(i)
        if(i==4):
            print(sad)
except Exception as error:
    print(error)

#让异常后的程序继续
for i in range(0,10):
    try:
        print(i)
        if(i==4):
            print(opo)
    except Exception as err:
        print(err)
print("loop end")
        