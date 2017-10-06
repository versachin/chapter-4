import turtle
wn = turtle.Screen()
s = turtle.Turtle()

def make_square(sz):
       for i in range(4):
        s.pendown()
        s.forward(sz)
        s.left(90)
make_square(20)
s.penup()
s.setx(-20)
s.sety(-20)
make_square(60)
s.penup()
s.setx(-40)
s.sety(-40)
make_square(100)
s.penup()
s.setx(-60)
s.sety(-60)
make_square(140)
s.penup()
s.setx(-80)
s.sety(-80)
make_square(180)


