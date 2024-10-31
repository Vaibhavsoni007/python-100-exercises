"""Write a program that calculates the kinetic energy of a
moving object, using the formula E = (mv²) / 2, where E is the
kinetic energy, m is the mass of the object, and v is the velocity."""

m = float(input("Enter the mass of object : "))
v = float(input("Enter the velocity of object : "))
E = (m*v**2)/2
print(f"the kinetic energy will be : {E} joules")