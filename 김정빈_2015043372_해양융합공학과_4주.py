guguLine, guguNum = "", ""

for i in range(1, 10):
    if i > 1:
        guguLine += f"# {i}단 # "
    for j in range(2, 10):
        if i * j < 10:
            guguNum += f"{j}* {i}= {i*j} "
            if j == 9:
                guguNum += "\n"
        elif i == 9 and j == 9:
            guguNum += f"{j}* {i}={i*j}"
        elif j == 9:
            guguNum += f"{j}* {i}={i*j} \n"
        else:
            guguNum += f"{j}* {i}={i*j} "

print(guguLine)
print(guguNum)

guguLine = ""
for i in range(2, 10):
    guguLine = guguLine + (" # %d단 #" % i)
print(guguLine)

for i in range(1, 10):
    guguLine = ""
    for k in range(2, 10):
        guguLine = guguLine + ("%2d*%2d=%2d" % (k, i, k * i))
    print(guguLine)