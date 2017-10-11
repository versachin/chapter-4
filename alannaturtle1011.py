import turtle
wn= turtle.Screen()
wn.bgcolor("hotpink")
alanna=turtle.Turtle()
alanna.pensize(3)
def draw_poly(turt,num,size):
    for i in range(num):
        turt.forward(size)
        turt.left(360/num)
draw_poly(alanna,8,50)

