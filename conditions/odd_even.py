"""Write a program that reads a number and reports whether it is odd or
even"""

num = int(input("Enter a number : "))
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")