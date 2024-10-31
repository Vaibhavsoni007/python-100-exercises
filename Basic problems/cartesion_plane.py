"""Write a program that reads the x and y position of two
points in the Cartesian plane, and calculates the distance
between them."""

x1 = int(input("enter the x co-ordinates of point 1 : "))
y1 = int(input("enter the y co-ordinates of point 1 : "))

x2 = int(input("enter the x co-ordinates of point 2 : "))
y2 = int(input("enter the y co-ordinates of point 2 : "))

d = ((x2-x1)**2  +  (y2-y1)**2)**0.5
print(f"the distance is {d:.2f}")





