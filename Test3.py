""" a=int(input())
b=int(input())
if(a>b):
    print(a-b)
else:
    print(a+b) """

""" x="hyrathon"
i='y'
while i in x:
    x=x[:-1]
    print(i,end="") """

""" lst1=[1,2,3]
lst2=[4,5,6]
result=[x*y for x in lst1 for y in lst2]
print(result) """

""" def func(i,x=[]):
    x.append(i)
    return x
for i in range(3):
    y=func(i)
print(y) """

""" def func():
    try:
        return 1
        print(5/0)
    except:
        print(2)
    finally:
        print(3)
        return 4
x=func()
print(x) """

""" class Parent:
    def __init__(self):
        self.x=1
    def change(self):
        self.x=10
class Child(Parent):
    def change(self):
        self.x=self.x+1
        return self.x
obj=Child()
print(obj.change()) """

""" class A:
    def __init__(self,x):
        self.x=x
    def count(self,x):
        self.x+=1
class B(A):
    def __init__(self, y):
        A.__init__(self,3)
    def count(self,x):
        self.y+=1

obj=B()
obj.count()
print(obj.x,obj.y) """

class Cls():
    def __init__(self,count=0):
        self.__count=count
a=Cls(2)
b=Cls(2)
print(id(a)==id(b),end="")
c="hello"
d="hello"
print(id(c)==id(d),end="")