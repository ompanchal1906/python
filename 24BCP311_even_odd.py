import random
od=[random.choice(range(1,1000,2))  for i in range(5) ]
print(od)
ev=[random.choice(range(2,1000,2))  for i in range(4) ]
print(ev)
od[2]=[*ev]
print(od)
flattern=[]
for i in od:
    if isinstance(i,list):
        flattern.extend(i)
    else:
        flattern.append(i)
flattern.sort() 
print(flattern)
