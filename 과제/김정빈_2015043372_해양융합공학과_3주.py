english_score = int(input("Please input ENG score : "))
math_score = int(input("Please input MATH score : "))


if english_score + math_score >= 110:
    if english_score < 40:
        print("Your 'ENG' score is less then standard.")
    elif math_score < 40:
        print("Your 'MATH' score is less then standard")
    else:
        print("Congraturations, You Passed!")

else:
    print("Your 'TOTAL' score is less then standard")
