def pel(x):
    reve = x[::-1]
    if x == reve:
        print("string is palindrome")
    else:
        print("string is not palindrome")
x = str(input("Enter string: "))
pel(x)
