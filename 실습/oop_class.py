class Car:

    color = ""
    speed = 0
    alias = "부릉이"

    def __init__(self, color_value, speed_value):
        self.color = color_value
        self.speed = speed_value

    def upSpeed(self, value):
        self.speed += value

    def __str__(self):
        return self.alias


Ferrari = Car("빨강", 30)
Porche = Car("노랑", 120)

Ferrari.upSpeed(50)

print(Ferrari)
print(Porche.speed)