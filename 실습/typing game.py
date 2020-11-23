import random
import time

w = ["cat", "생쥐", "사자", "코끼리"]
i = 1
input("[타자 게임] 준비되면 엔터를 누르세요.")
start = time.time()
while i <= 5:
    print(f"* 문제{i}")
    list_index = random.randint(0, len(w) - 1)
    answer = input(f"{w[list_index]} \n=")
    if answer == w[list_index]:
        print("통과!")
        i += 1
    else:
        print("오타입니다. 다시해보세요!")
end = time.time()

et = round((end - start), 2)
print(f"총 시간은 {et}초 걸렸습니다.")