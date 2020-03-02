class cl1:
    pass

#实例化 a=cl1()

#构造函数
#__init__(self,参数)
#self：在类中的方法必须加上self
class cl2:
    def __init__(self):
        print("I am cl2!")

#给类加上参数：给构造方法加上参数

class cl3:
    def __init__(self,name,job):
        print("My name is "+name+"My Job is "+job)

class cl4:
    def __init__(self,name,job):
        self.myname=name
        self.myjob=job

#方法：类里面的函数
# def 函数名（self,参数）
class cl5:
    def myfunc(self,name):
        print("hello"+name)       
class cl6:
    def __init__(self,name):
        self.myname=name
    def myfunc(self):
        print("hello "+self.myname)


#继承与重载
#单继承，多继承
class person():
    def __init__(self):
        print("我是人")
    def walk(self):
        print("我会走路")

class father(person):
    def __init__(self):
        print("我是父亲")
    def speak(self):
        print("我可以说话")
class mother(person):
    def __init__(self):
        print("我是母亲")
    def cook(self):
        print("我会做饭")
class son(father):
    def __init__(self):
        print("我是儿子")
class daughter(father,mother):
    def __init__(self):
        print("我是女儿")
    def sing(self):
        print("我会唱歌")

#重写（重载）
class son2(father):
    def __init__(self):
        print("我是弟弟")
    def speak(self):
        print("我会演讲")