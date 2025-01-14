import turtle
t = turtle.Pen()
t.reset()
for x in range(1,9):
    t.forward(45)
    t.left(45)

t.reset()
def myoctagon(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1,9):
        t.forward(50)
        if x % 2 == 0:
            t.left(45)
        else:
            t.left(45)
    if filled == True:
        t.end_fill()
t.color('#d40404')
myoctagon(50, True)
t.color(0, 0, 0)
myoctagon(50, False)

t.reset()
for x in range(1,73):
    t.forward(150)
    if x % 2 == 0:
            t.left(175)
else:
            t.left(225)
