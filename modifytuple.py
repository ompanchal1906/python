#6.	Modify an element of a tuple.
a=(1,2,3,4,5)
b=list(a)
b[2]=10
a=tuple(b)
print(a)