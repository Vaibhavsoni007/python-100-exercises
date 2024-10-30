"""Write a program that calculates the perimeter and area of a
is the width and l is the length
rectangle, using the formulas P = 2(w + l) and A = wl, where w"""

w = float(input("Enter the width of the rectangle : "))
l = float(input("Enter the lenght of the rectangle : "))

perimeter = 2*(w + l)
area = w*l

print(f"the area of rectangle is {area} \nand perimeter is {perimeter}")
