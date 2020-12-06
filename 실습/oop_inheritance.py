class Car:
    speed = 0

    def __init__(self):
        Car.speed = 30

    def upSpeed(self, value):
        self.speed = value
        print(f"슈퍼 클래스의 속도는 {self.speed}")


class Sedan(Car):
    pass


class Truck(Car):
    def upSpeed(self, value):
        self.speed = value
        print(f"서브 클래스의 속도는 {self.speed}")


sedan1 = Sedan()
print("===세단===")
sedan1.upSpeed(50)

truck1 = Truck()
print("===트럭===")
truck1.upSpeed(100)

cha = Car()
print("===그냥 차===")
print(cha.speed)