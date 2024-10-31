"""Create a program that prompts the user for the radius of a
sphere and calculates and displays its volume."""

r = float(input("Enter the radius of the sphere : "))
volume = (4*3.14*r**3)/3
print(f"the volume of the sphere is : {volume:.2f}")