import random
num=[random.choice(range(1,100,1)) for i in range(20)]
print(num)
x=int(input("enter number"))
print(num.index(x))
