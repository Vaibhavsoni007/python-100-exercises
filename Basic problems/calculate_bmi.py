"""Write a program that calculates the BMI of an individual,
using the formula BMI = weight / height²"""

weight = float(input("Enter your weight : "))
height = float(input("Enter your height (in m) : "))
bmi = weight/height**2
print(f"your bmi is : {bmi}")