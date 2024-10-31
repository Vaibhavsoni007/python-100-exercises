"""Write a program that calculates the average velocity of an
object, using the formula v = Δs/Δt, where v is the average
velocity, Δs is the space variation, and Δt is the time variation"""

space_variation = float(input(f"{'Enter the space variation : ':<30}"))
time_variation = float(input(f"{'Enter the time variation : ':<30}"))
delta = space_variation/time_variation

print(f"{'average velocity is :':<29} {delta:.2f}")