import turtle
wn = turtle.Screen()
s = turtle.Turtle()
s.pensize(3)
s.color("hotpink")
wn.bgcolor("lightgreen")
def draw_poly(t,num,sz):
    for i in range(num):
        t.forward(sz)
        t.left(360/num) 
def draw_equitriangle(t, sz):
    draw_poly(s,3,100)
    
    
draw_equitriangle(s, 100)
    

