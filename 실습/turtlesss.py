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
    t.speed(0)
    for i in range(50):
        t.circle(80)
        t.left(360 / 50)


def diTri():
    t.speed(0)
    t.right(120)
    for i in range(200):
        if i % 3 == 0:
            t.color("red")
        if i % 3 == 1:
            t.color("yellow")
        if i % 3 == 2:
            t.color("blue")
        t.forward(i * 4)
        t.left(121)


diTri()