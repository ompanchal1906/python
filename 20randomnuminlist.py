#2.	Generate 20 random integers and store them in a list.
#  Accept a number from the user and print position of all occurrences of that number in the list.
import random
number=[]
for i in range(20):
    number.append(random.choice(range(1,1000,1)))
print("list of 20 number is:",number)
num=int(input("enter the number to find it's position:"))
position=[]
p=number.index(num)
print("position of number",num,"is",p)
#for i in range(20):
 #   if number[i]==num:
  #      position.append(i)
#print("position of number",num,"is",position)