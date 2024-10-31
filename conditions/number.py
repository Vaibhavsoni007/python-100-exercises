"""Write a program that reads a number and reports whether it is positive,
negative or zero."""

num = float(input("Enter a number : "))

if num==0:
    print(f"{num} is zero")
elif num<0:
    print(f"{num} is negative")
else:
    print(f"{num} is positive")
