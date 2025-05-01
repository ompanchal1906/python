#creat an empty set .write a program that adds five new nanes to this set , modifies one existing name and remove two name from it.
empty=set()
for i in range(5):
    name=input("Enter name :")
    empty.add(name)
print("your set is:",empty)
remove=input("Which one name you would like to change:")
empty.discard(remove)
new_name=input("Enter new name:")
empty.add(new_name)
print("your new set is:",empty)
for i in range(2):
    remove=input("Which one name you would like to remove:")
    empty.discard(remove)
print("your new set by removing name is:",empty)