"""Write a program that calculates the perimeter and area of a
triangle, using the formulas P = a + b + c and A = (b * h) / 2,
where a, b and c are the sides of the triangle and h is the height
relative to the side B"""

a = float(input("enter the lenght of side a : "))
b = float(input("enter the lenght of side b : "))
c = float(input("enter the lenght of side c : "))
h = float(input("enter the height h : "))

perimeter = a + b + c
area = (b * h)/2

print(f"the area of the triangle is {area} and perimeter is {perimeter}")





