#4.	Generate 30 random numbers and put them in a list. 
# Create two more lists – one containing only +ve numbers and another with –ve nos.
import random
number=[]
for i in range(30):
    number.append(random.choice(range(-100,100,1)))
print("list of 30 number is:",number)
positive=[]
negetive=[]
for p in number:
    if p>0:
        positive.append(p)
    else:
        negetive.append(p)
print("list of positive numbers is:",positive)
print("list of negetive numbers is:",negetive)