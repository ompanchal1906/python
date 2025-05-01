#3.	Suppose a date is represented as a tuple (d, m, y).
#  Create two date tuples and find the number of days between the two dates.
a=(9,2,2020)
b=(12,1,2021)
print(a[2])
for i in a:
    i=str(a)
    j=str(b)
    for j in b:
        i=str(a)
        j=str(b)
        m=int(i[0])
        n=int(j[0])
        if i[0]>j[0]:
            p=int(i[0])-int(j[0])
        else:
            p=int(j[0])-int(i[0])
q=p*30
print("days between the two dates are:",q)
    
