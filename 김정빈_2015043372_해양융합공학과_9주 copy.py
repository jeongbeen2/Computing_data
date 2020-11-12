import random


ran_num = random.randint(1, 10)
num = [1, 2, 3, 4, 5, 6]
a = list(filter(lambda ran_num: ran_num not in num, num))

print(a)