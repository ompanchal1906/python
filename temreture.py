#6.	Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.

fahrenheit=[]
for i in range(10):
    fahrenheit.append(float(input("enter the temperature in fahrenheit:")))
print("list of temperatures in fahrenheit is:",fahrenheit)
celsius=[]
for i in fahrenheit:
    celsius.append((i-32)*5/9)
print("list of temperatures in celsius is:",celsius)