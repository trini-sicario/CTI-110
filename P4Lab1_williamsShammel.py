# Williams Shammel
# 12 october 2026
# Drawing shapes using loops

import turtle

# Set up turtle drawing objects
window = turtle.Screen()

Mikei = turtle.Turtle()

# change the turtle's color and size
Mikei.pensize(3)
Mikei.pencolor("orange")


# Use a for loop to draw a square
for i in range(4):
    Mikei.forward(200)
    Mikei.right(90)
    
# Use a while loop to draw a triangle
num = 1
while num <= 3:
    Mikei.forward(200)
    Mikei.left(120)
    num += 1

# Keep this at the bottom
window.mainloop()