#5.	A list contains 5 strings. Convert all these strings to uppercase.

lst=[]
lst2=[]
for i in range(5):
    lst.append(input("enter the string:"))
print("list of 5 strings is:",lst)
for i in lst:
    lst2.append(i.upper())
print(lst2)