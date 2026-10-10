import turtle
import random

t = turtle.Turtle()

t.shape('turtle')
t.speed(0)

c_list = ['red', 'blue', 'gold', 'cyan', 'magenta', 'skyBlue', 'gray', 'black', 'purple', 'orange']

r = 50
i =0

while i < 360:
    t.fillcolor(random.choice(c_list))

    t.begin_fill()
    t.circle(r)
    t.end_fill()
    r += 0.01
    i += 0.01
    t.right(i)


turtle.done()