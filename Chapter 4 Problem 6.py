import turtle
wn = turtle.Screen()
s = turtle.Turtle()
s.pensize(3)
s.color("hotpink")
wn.bgcolor("lightgreen")
def draw_equitriangle(t, sz):
    for i in range(3):
        t.forward(sz)
        t.left(360/3)
        
draw_equitriangle(s, 100)