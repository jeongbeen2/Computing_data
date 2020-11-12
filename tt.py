import random

while True:
    n = int(input("게임 수 : "))
    if n <= 0:
        break
    for _ in range(n):
        num = []
        while len(num) < 6:
            ran_num = random.randint(1, 45)
            if ran_num not in num:
                num.append(ran_num)
        print(sorted(num))