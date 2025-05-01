#write a program that converts words present in a list into uppercase an dstores them in a set

a=['prince','sohan','malay','om']
b=set()
for i in a:
    b.add(i.upper())

print(b)