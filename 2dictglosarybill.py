a={ "milk":32,'sugar':200,"rice":60}
b={"milk":3,'sugar':2,'rice':2}
c={}
total=0
for i,j in a.items():
    if i in b:
        c[i]=j*b[i]
        total=total+c[i]
print(c)
print("your bill is:",total)