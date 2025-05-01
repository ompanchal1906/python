def stri(n):
    n1=n
    n2=(str(n)*2)
    n3=(str(n)*3)
    n4=(str(n)*4)
    return int(n1)+int(n2)+int(n3)+int(n4)

for i in range(4,8):
    print(i,"=",stri(i))