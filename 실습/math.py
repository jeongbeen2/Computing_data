import turtle as t

t.shape("turtle")


def dohyeong(n):
    t.color("purple")
    for i in range(n):
        t.forward(100)
        t.left(360 / n)


def circle():
    t.bgcolor("black")
    t.color("green")
    t.speed(1)
    for i in range(50):
        t.circle(80)
        t.left(360 / 50)


circle()