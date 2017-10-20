#Extend your program above
#turn right by 144, put the pen down, and draw the next star. You’ll get something like this:
import turtle
alex=turtle.Turtle()
def draw_star():
    alex.right(216)
    for i in range(4):
        alex.forward(100)
        alex.left(216)
    alex.forward(100)
draw_star()