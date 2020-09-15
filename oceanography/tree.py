treeHit = 1

while treeHit <= 10:
    print(f"나무를 {treeHit}번 찍었습니다.")

    if treeHit == 5:
        print("나무가 흔들립니다!")
    elif treeHit == 8:
        print("나무가 곧 쓰러질 것 같습니다.")
    elif treeHit == 10:
        print("나무가 쓰러졌습니다!")
    treeHit += 1