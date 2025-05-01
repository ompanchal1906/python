def count_alpha_digits(x):
    dic={}
    for i in x:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic
x=str(input("enter your string:"))
print(count_alpha_digits(x))
