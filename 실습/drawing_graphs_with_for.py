import turtle as t

x_min, y_min = -5, -5
x_max, y_max = 5, 5
space = 0.1

fun = ["y=abs(x)", "y=x*x"]

t.setworldcoordinates(x_min, y_min, x_max, y_max)

t.pensize(2)

t.up()
t.goto(x_min, 0)
t.down()
t.goto(x_max, 0)

t.up()
t.goto(0, y_min)
t.down()
t.goto(0, y_max)

t.color("green")

for i in fun:
    x = x_min
    exec(i)  # y값 설정해 주는것.
    t.up()
    t.goto(x, y)
    t.down()

    while x <= x_max:
        x += space
        exec(i)
        t.goto(x, y)
