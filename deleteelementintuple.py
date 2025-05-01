#7.	Delete an element of a tuple.
a=(1,2,3,4,5)
b=list(a)
b.clear()
a=tuple(b)
print(a)