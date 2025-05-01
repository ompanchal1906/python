def ran():
    import random
    y=[]
    p=[]
    for i in range(10):
        x=random.choice(range(-15,15))
        y.append(x)
    print(y)
    for i in y:
        w=i*i
        p.append(w)
    print(p)
ran()