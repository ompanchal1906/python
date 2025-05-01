#3.	Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list.

import random
number=[]
for i in range(50):
    number.append(random.choice(range(1,30,1)))
print("list of 50 number is:",number)
p=set(number)
print(p)
print("list after removing duplicate values",list(p))