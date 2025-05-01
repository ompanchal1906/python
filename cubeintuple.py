def num(x):
    lst=[]
   #p=()
    for i in range(1,x+1):
        p=(i,i**2,i**3)
        lst.append(p)
    return lst
x=int(input("Enter your numer:"))
print(num(x))
