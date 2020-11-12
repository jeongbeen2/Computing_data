import random


def lotto_game():
    print("#### Lotto Game Start ####")
    while True:
        n = int(input("<1>로또 수동 <2>로또 자동 <3>로또 종료 \n >>> 번호입력 : "))
        if n == 3:
            print("로또를 종료합니다.")
            break
        elif n == 1:
            print("수동 기능은 차후 업데이트 예정입니다. 자동기능을 사용해 주세요.")
        elif n == 2:
            while True:
                auto = int(input("뽑고자 하는 로또 갯수를 입력하세요 : "))
                if auto <= 0:
                    print("로또를 종료합니다.")
                    break
                for _ in range(auto):
                    num = []
                    while len(num) < 6:
                        ran_num = random.randint(1, 45)
                        if ran_num not in num:
                            num.append(ran_num)
                    print(sorted(num))
                print("대박 나세요! \n")
            break
        else:
            print("잘못된 숫자 입력입니다. 다시 입력해 주세요.")


lotto_game()