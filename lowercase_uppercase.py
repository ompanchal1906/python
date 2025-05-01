def up(x):
    upp=0
    low=0
    for i in x:
        #print(i)
        if i.isupper():
            upp=upp+1
        elif i.islower():
            low=low+1
        dict={"upper":upp,"lower":low}
    print(dict)
x=str(input("Enter any string:"))
up(x)