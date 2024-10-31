"""Make a program that asks for a person's age and displays whether they
are of legal age or not."""

age = int(input("Enter the age : "))

if age>18:
    print("your age is legal")
else:
    print("your age is illigal")