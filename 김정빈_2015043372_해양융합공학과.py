pencil = 1000
pen = 2000
pencil_count = int(input("연필의 갯수를 입력해주세요 : "))
pen_count = int(input("펜의 갯수를 입력해주세요 : "))
total_count = pencil * pencil_count + pen * pen_count

print("총 가격은 %s 원 입니다." % total_count)

# use f-string
# print(f"총 가격은 {total_count} 원 입니다.")
