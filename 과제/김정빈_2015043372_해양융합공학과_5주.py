while True:
    a = int(input("첫 번째 수 입력: "))
    b = int(input("두 번째 수 입력: "))
    ch = input("계산할 연산자를 입력: ")

    if ch == "+":
        print("%d + %d = %d 입니다." % (a, b, a + b))
        break
        # break를 해주지 않으면 Error가 날 때까지 while문이 무한으로 돌아감.
    elif ch == "-":
        print("%d - %d = %d 입니다." % (a, b, a - b))
        break
    elif ch == "*":
        print("%d * %d = %d 입니다." % (a, b, a * b))
        break
    elif ch == "/":
        print("%d / %d = %s 입니다." % (a, b, a / b))
        break
        # %d 는 정수형 인자만 받기 때문에, 나누는 부분은 %d보다 %.1f, 혹은 %s를 써야 더 자세히 나온다.
    elif ch == "//":
        print("%d // %d = %d 입니다." % (a, b, a // b))
        break
    elif ch == "%":
        print("%d %% %d = %d 입니다." % (a, b, a % b))
        # print 내에있는 연산자 %는 %d의 %와 겹치므로, %%을 사용해 주어야함.
        break
    elif ch == "**":
        print("%d ** %d = %d 입니다." % (a, b, a ** b))
        break
    else:
        print("연산자 잘못 입력")
        break
