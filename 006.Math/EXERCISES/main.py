# EXERCISE 1
# Calculate the circumference of a circle / formula = 2 * r * pi

import math

radius = float(input("Enter the radius of a circle:"))

circumference = 2 * math.pi * radius

print(f"The circumference is {round(circumference , 2)}cm") #round by 2 decimal digits

# EXERCISE 2
# Calculate the area of a circle / formula = pi * r * r

radius2 = float(input("Enter the radius of a circle:"))

area = math.pi * radius2 * radius2

print(f"The area of the circle is {round(area , 2)}cm^2")

# EXERCISE 3
# Calculate the hypotenuse of a right triangle / formula = c = square root of a^2 + b^2

a = float(input("Enter side A:"))
b = float(input("Enter side B:"))

c = math.sqrt(pow(a , 2) + pow(b , 2))

print(f"Side C = {c}")