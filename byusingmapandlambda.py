import random
p=[]
for i in range(10):
    x=random.choice(range(-15,15))
    p.append(x)
print(p)
m=map(lambda x:x*x,p)
print(list(m))