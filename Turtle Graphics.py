import turtle
turtle.bgcolor("black")

squary = turtle.Turtle()
squary.speed(100)
squary.pencolor("darkred")
for i in range(10000):
    squary.forward(i)
    squary.pencolor("darkred")
    squary.left(93)
    squary.circle(3)
    squary.pencolor("red")