while True:
    a = int(input("첫 번째 수 입력: "))
    b = int(input("두 번째 수 입력: "))
    ch = input("계산할 연산자를 입력: ")

    if ch == "+":
        print("%d + %d = %d 입니다." % (a, b, a + b))
        break  # break를 해주지 않으면 잘못된 값을 입력할 때 까지 while문이 무한으로 돌아감.
    elif ch == "-":
        print("%d - %d = %d 입니다." % (a, b, a - b))
        break
    elif ch == "*":
        print("%d * %d = %d 입니다." % (a, b, a * b))
        break
    elif ch == "/":
        print("%d / %d = %d 입니다." % (a, b, a / b))
        break
    elif ch == "//":
        print("%d // %d = %d 입니다." % (a, b, a // b))
        break
    elif ch == "%":
        print(
            "%d %% %d = %d 입니다." % (a, b, a % b)
        )  # print 내에있는 %는 %d와 겹치므로, %%를 사용해 주어야함.
        break
    elif ch == "**":
        print("%d ** %d = %d 입니다." % (a, b, a ** b))
        break
    else:
        print("연산자 잘못 입력")
        break