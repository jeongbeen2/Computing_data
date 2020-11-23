import turtle as t

x_min = -5
x_max = 5

y_min = -5
y_max = 5

space = 0.1

fun = "y=abs(x)"

t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.pensize(2)

t.up()
t.goto(x_min, 0)
t.down()
t.goto(x_max, 0)

t.up()
t.goto(x_min, 0)
t.down()
t.goto(x_max, 0)

x = x_min
exec(fun)
t.up()
t.goto(x, y)
t.down()

while x <= x_max:
    x = x + space
    exec(fun)
    t.goto(x, y)
