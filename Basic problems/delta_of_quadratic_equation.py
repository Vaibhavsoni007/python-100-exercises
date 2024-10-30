"""Write a program that calculates the delta of a quadratic
equation (Δ = b² - 4ac)."""

b = int(input("Enter the value of b : "))
a = int(input("Enter the value of a : "))
c = int(input("Enter the value of c : "))
delta = ((b**2) - 4*a*c)
print(f"the delta of the quadratic equation will be : {delta}")