#Write a void function to draw a star,
#where the length of each side is 100 units.
#(Hint: You should turn the turtle by 144 degrees at each point.)
import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
alex=turtle.Turtle()
alex.color("hotpink")
alex.pensize(3)
def draw_star():
    alex.right(216)
    for i in range(4):
        alex.forward(100)
        alex.left(216)
    alex.forward(100)
for i in range(5):
    alex.penup()
    alex.left(144)
    alex.forward(350)
    alex.pendown()
    draw_star()
