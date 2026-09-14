# Williams Shammel
# 14 September 2026
# Calculations for a circle

# import the value for pi
from math import pi
print(pi)

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# show data type of the radius
print(type(radius))


print()
# show data type of the radius
print(type(radius))

# Calculate the diameter of the circle

diameter = 2 * radius

# Display the diameter of the circle using the f-string
print(f"The diameter of the circle is: {diameter:.1f}")

print()

# Calculate the circumference of the circle
circumference = 2 * pi * radius

# Display the circumference of the circle using the f-string
print(f"The circumference of the circle is: {circumference:.2f}")

# Calculate the area of the circle
area = pi * radius ** 2

print()

# Display the area of the circle using the f-string
print(f"The area of the circle is: {area:.3f}")