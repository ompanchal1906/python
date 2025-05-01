#write a charactor from the key board
a=input("Enter the string")
b={}
for i in a:
    if i in b:
        b[i]=b[i]+1
    else:
        b[i]=1
print(b)