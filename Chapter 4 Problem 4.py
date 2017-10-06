import turtle
wn = turtle.Screen()
s = turtle.Turtle()
def make_square(sz):
       for i in range(4):
        s.pendown()
        s.forward(sz)
        s.left(90)
for i in range(20):
    make_square(100)
    s.left(20)