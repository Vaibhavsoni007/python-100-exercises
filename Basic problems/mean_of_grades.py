"""Create a program that calculates and displays the arithmetic
mean of three grades entered by the user"""

print("--------Enter the grades out of 10--------")
grade1 = int(input("Enter the grade 1 : "))
grade2 = int(input("Enter the grade 2 : "))
grade3 = int(input("Enter the grade 3 : "))

mean = (grade1+grade2+grade3)/3
print(f"the mean of the grades is : {mean}")