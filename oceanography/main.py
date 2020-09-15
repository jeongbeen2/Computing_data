# temp = ["2020.09.14", 20, 18, 17.5, 22.5, 24, 22]

# print(temp[1:])

# a = [1, 2, 3]


# a.insert(0, 1)

# print(a)

# date2020 = ["2020.02.27", "2020.02.28", "2020.03.01"]

# date2020.insert(2, "2020.02.29")

# print(date2020)

# a = ["a", "b", "c", "d", "b", "a"]

# a.remove("b")
# print(a)
# a.pop(1)

# date2019 = ["2019.02.28", "2019.02.29", "2019.03.01"]

# # date2019.remove("2019.02.29")

# date2019.pop(1)

# print(date2019)

# a = [1, 1, 1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 7]

# b = a.index(5)
# print(b)

# temp = [22, 22.5, 23, 22, -999, 22.5, 24, 26, 27, 26.5]

# temp.pop(temp.index(-999))

# total = 0

# for i in temp:
#     total += i

# result = round(total / len(temp), 1)

# print(result)


# import numpy

# temp = [22, 22.5, 23, 22, -999, 22.5, 24, 26, 27, 26.5]

# temp.pop(temp.index(-999))
# result = numpy.mean(temp)

# print(result)
import numpy

temp = [22, 22.5, 23, 22, -999, 22.5, -999, 24, 26, 27, -999, 26.5]
# missing = []
# for i in temp:
#     if i == -999:
#         a = temp.index(-999)
#         missing.append(a)
#         temp.remove(-999)
# mean = round(numpy.mean(temp), 1)

# print("The Missing Data index is :", *missing)
# print(f"The mean value : {mean}")

temp_np = numpy.array(temp)

print(temp_np == -999)