import turtle
t = turtle.Pen()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

t.reset()
t.backward(100)
t.up()
t.right(90)
t.forward(20)
t.left(90)
t.down()
t.forward(100)

t.reset()
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)

t.reset()
t.forward(90)
t.left(90)
t.forward(60)
t.left(90)
t.forward(90)
t.left(90)
t.forward(60)

t.reset()
for x in range (0, 4):
    t.forward(50)
    t.up()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.down()



