import turtle as t

# quadrant min/max
x_min, y_min = -5, -5
x_max, y_max = 5, 5

# graph settings
space = 0.1
t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.pensize(2)
t.speed(0)

# I love turtle
t.shape("turtle")

# drawing quadrant X-axis
t.up()
t.goto(x_min, 0)
t.down()
t.goto(x_max, 0)

# drawing quadrant Y-axis
t.up()
t.goto(0, y_min)
t.down()
t.goto(0, y_max)

# graph colors
color_list = [
    "red",
    "green",
    "blue",
    "black",
    "purple",
]

# functions
fun_list = [
    "y=abs(x)",
    "y=x**2",
    "y=(0.5*x)+1",
]

# function initial value
n = 0
while n <= len(fun_list) - 1:
    x = x_min
    t.color(color_list[n % len(color_list)])
    fun = fun_list[n]
    exec(fun_list[n])
    t.up()
    t.goto(x, y)
    t.down()

    # drawing graph
    while x <= x_max:
        x = x + space
        exec(fun_list[n])
        t.goto(x, y)
    n += 1