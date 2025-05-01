#1.	Write a program to create three dictionaries and concatenate them to create fourth dictionary.

dict1 = {1: 'a', 2: 'b'}
dict2 = {3: 'c', 4: 'd'}
dict3 = {5: 'e', 6: 'f'}
dict4 = {}
for i in (dict1,dict2,dict3):
    dict4.update(i)

print(dict4)