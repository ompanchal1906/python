#1.	A list contains names of boys and girls as its elements. 
# Boys’ names are stored as tuples.
#  Write a program to find out number of boys and girls in the list.
#  (Hint: use isinstance(ele,tuple))

a=[('ram',),('shyam',),('mohan',),'sita','gita','rita','preet']
count=0
for i in a:
    if isinstance(i,tuple):
        count+=1
print("there are",count,"boys")
co=0
for i in a:
    if isinstance(i,str):
        co+=1
print("there are",co,"girls")