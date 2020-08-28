import turtle

t = turtle.Turtle()

t.color("red","yellow")
t.begin_fill()

for i in range(50):
    t.forward(300)
    t.left(170)

t.end_fill()
turtle.done()
