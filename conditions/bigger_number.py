"""Write a program that reads two numbers and tells you which one is
bigger."""

num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))

if num1>num2:
    print(f"{num1} is bigger than {num2}")
elif num1<num2:
    print(f"{num2} is bigger than {num1}")
else:
    print("both are equal")