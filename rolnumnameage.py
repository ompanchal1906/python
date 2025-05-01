#2.	A list contains tuples containing roll no., name and age of student.
#  Write a python program to create three lists separately for roll no., name and age
a=[(212,'ram',20),(215,'shyam',81),(313,'mohan',25),(428,'sita',46),(511,'gita',89)]
b,c,d=[],[],[]
for i in a:
    b.append(i[0])
    c.append(i[1])
    d.append(i[2])

print("roll no. list:",b)
print("name list:",c)
print("age list:",d)