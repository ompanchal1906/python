#define three function fun(),disp(),msg(), store them in a list and call them one by one
def fun():
    print("hello")
def disp():
    print("world")
def msg():
    print("hii")
p=fun()
q=disp()
r=msg()
lst=[p,q,r]
for i in lst:
    i()