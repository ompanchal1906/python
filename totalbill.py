#5.	Create two dictionaries – one containing grocery items and their
#  prices and another containing grocery items and quantity purchased. 
# By using the values from these two dictionaries compute the total bill.
a={"apple":100,"banana":50,"orange":80,"grapes":120}
b={"apple":2,"banana":3,"orange":4,"grapes":5}
for i in a:
    total=0
    for j in b:
        total=total+(a[j]*b[j])

print("Total bill:",total)







#for i in b:
    #total=0
    #for j in a:
     #   total=total+(a[j]*b[j])
#print(b)

#print("Total bill:",total)