import random

com_number = random.randint(1, 100)


def is_same(target, number):
    if target == number:
        result = "Win"
    elif target > number:
        result = "High"
    else:
        result = "Low"
    return result


print("1부터 100중 숫자 하나를 골랐습니다.")

number_of_times = 0
weird = 0
while True:
    guess = int(input("1부터 100 중 숫자를 입력하고 엔터키를 클릭하세요 : "))
    if guess > 100 or guess < 0:
        print("1~100의 숫자를 입력하세요. 입력하신 숫자는 범위 밖입니다.")
        weird += 1
        number_of_times += 1
    else:
        h_or_l = is_same(com_number, guess)
        if h_or_l == "Win":
            print("정답 입니다.")
            print(f"총 {number_of_times}번 만에 맞추셨습니다.")
            print(f"범위밖의 숫자를 {weird}번 입력하셨습니다.")
            break
        elif h_or_l == "High":
            print("\n입력하신 숫자보다 더 큰(BIGGER) 숫자입니다.")
            print("다시 추측해 볼까요? \n ")
        elif h_or_l == "Low":
            print("\n입력하신 숫자보다 더 작은(SMALLER) 숫자입니다.")
            print("다시 추측해 볼까요? \n")
        number_of_times += 1
