#5.	Remove empty tuple(s) from the list of tuples.
a=[('ram',),('shyam',),(),'sita','gita','rita','preet',()]
b=[]
for i in a:
    if i!=():
        b.append(i)
print(b)