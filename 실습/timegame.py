import time


times = int(input("측정할 시간을 적어주세요"))
input("엔터를 누르면 시작합니다.")
start = time.time()
input(f"{times}초뒤 눌러보세요.")
end = time.time()
total = round((end - start), 2)
error = abs(times - total)

if error < 0.5:
    print(f"오차는 {error}초로, 잘 하셨네요!")

else:
    print(f"오차는 {error}초로, 분발하세요!")
