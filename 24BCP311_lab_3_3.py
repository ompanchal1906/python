def a(x,y):
    if x in y:
        print("your x string is in y string")
    elif y in x:
        print("your y string is in x string")
    else:
        print("there areb no same string")

x=input("enter first sring")
y=input("enter second string")
a(x,y)
