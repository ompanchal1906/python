def st(x):
    p=set(x)
    q=list(p)
    z=[]
    for i in range(65,123):
        if chr(i) in q:
            z.append(chr(i))
    print(z)
x=str(input("enter string:"))
st(x)