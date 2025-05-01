def a(x,y):
    if x in y:
        print(y.replace(x,""))
    elif y in x:
        print(x.replace(y,""))
    else:
        print("There are no same containt in that string")

x=input("enter first string")
y=input("enter second string")
a(x,y)
