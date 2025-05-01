#9.	Take two lists of numbers. Create third list of numbers for only those numbers from 
# first list which are not there in 2nd list (use list comprehension). 
a=[]
b=[]
c=[]
for i in range(5):
    a.append(int(input("enter the number in first list a:")))
for i in range(5):
    b.append(int(input("enter the number in second list b:")))
    
print("list a is:",a)
print("list b is:",b)
for i in a:
    if i not in b:
        c.append(i)
print("list c is:",c)
for i in b:
    if i not in a:
        c.append(i)
print("list c is:",c)