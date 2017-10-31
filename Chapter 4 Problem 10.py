#Extend your program above
#turn right by 144, put the pen down, and draw the next star. You’ll get something like this:
import turtle
alex=turtle.Turtle()
alex.color("hot pink")
alex.pensize(3)
wn=turtle.Screen()
wn.bgcolor("light green")
def draw_star():
    alex.right(216)
    for i in range(4):
        alex.forward(100)
        alex.left(216)
    alex.forward(100)
for i in range (5):
    draw_star()
    alex.penup()
    alex.forward(350)
    alex.right(144)
    alex.pendown()
                 