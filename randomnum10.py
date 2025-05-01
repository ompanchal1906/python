#take 10 randome number in range of 15 to 45. count how many of these numbe s are less than 30.delete all number that are greater than 35
import random
a=set()
b=set()
c=set()
for i in range(10):
    a.add(random.choice(range(15,45)))
print(a)
for i in a:
    if i<30:
        b.add(i)
c={num for num in a if num>=35}
#or
#for num in a:
#    if num>=35:
#        c.add(num)
print("your number less than 30 is:",len(b))
print("your set with number greater than 35 is",c)