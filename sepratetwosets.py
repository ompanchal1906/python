#a set  comtaim names which begin either with A or with B . write a program to seprate out the names into two sets,
# one containing names begining A and secone containing names begining with B.

a={'Amul',"Aman","Atri","Bhanu","Bhavya"}
b={name for name in a if name.startswith('A')}
b=set()
c=set()
for i in a:
    if i.startswith("A"):
        b.add(i)
print("your names which begins with A is:",b)
for i in a:
    if i.startswith("B"):
        c.add(i)
print("your names which begins with B is:",c)
