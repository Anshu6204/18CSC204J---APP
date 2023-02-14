import turtle
my_wn=turtle.Screen()
my_wn.title("Turtle")
my_pen=turtle.Turtle()
my_pen.color("black")

def rot_sqr(size,num):
    for i in range(num):
       my_pen.fd(size/2)
       my_pen.left(90)
       my_pen.fd(size)
       my_pen.left(90)
       my_pen.fd(size)
       my_pen.left(90)
       my_pen.fd(size)
       my_pen.left(90)
       my_pen.fd(size/2)
       my_pen.left(360/num)

rot_sqr(146,5)
