def grade_system():
    sub = ["국어", "수학", "영어", "컴퓨터", "환경화학", "고지자기학"]
    i = 0
    grade = []
    while i < len(sub):
        n = int(input(f"당신의 {sub[i]}점수를 입력하세요: "))
        if n > 100 or n < 0:
            print("입력값 오류")
        else:
            if n <= 100 and n >= 90:  # 90~100
                grade.append(f"당신의 {sub[i]} 학점은({n}) A입니다.")
            elif n < 90 and n >= 80:  # 80~90
                grade.append(f"당신의 {sub[i]} 학점은({n}) B입니다.")
            elif n < 80 and n >= 70:  # 70~80
                grade.append(f"당신의 {sub[i]} 학점은({n}) C입니다.")
            elif n < 70 and n >= 60:  # 60~70
                grade.append(f"당신의 {sub[i]} 학점은({n}) D입니다.")
            elif n < 60:
                grade.append(f"당신의 {sub[i]} 학점은({n}) F입니다.")
            i += 1

    for j in range(len(grade)):
        print(grade[j])


grade_system()
