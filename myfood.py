food = {
    "떡볶이": "오뎅",
    "짜장면": "단무지",
    "라면": "김치",
    "맥주": "치킨",
    "삼겹살": "소주",
}

while True:
    myfood = input(str(list(food.keys())) + "중 좋아하는 것은? :")

    if myfood in food:
        print("%s 와 궁합음식은 %s 입니다." % (myfood, food.get(myfood)))
    else:
        while True:
            a = input("맞는 음식을 찾을 수 없습니다. 그만 두시겠습니까? y/n: ")
            if a == "y":
                break
            elif a == "n":
                exit()
            else:
                print("y 혹은 n을 입력해주세요")
