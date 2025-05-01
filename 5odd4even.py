#1.	Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using random nos. 
# Replace the third element of odd integers with  
# a list of 4 even integers. Flattern, sort and print the list. Provide appropriate message at each stage.

import random
odd=[]
even=[]
for i in range(5) :
    odd.append(random.choice(range(1,100,2)))
print("list of 5 odd intergers",odd)
for i in range(4):
    even.append(random.choice(range(2,100,2)))
print("List of 4 even numbers:",even) 
odd[2]=even
print("list after replacing 3th element of odd with even",odd)
flattern=[]
for i in odd:
    if isinstance(i,list):
        flattern.extend(i)
    else:
        flattern.append(i)
print(flattern)
flattern.sort() 
print(flattern)
print("sorted list of odd and even numbers",flattern)
