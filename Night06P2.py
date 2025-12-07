import sys

lines = []
for line in sys.stdin:
    lines += [line.strip("\n").strip("\r")]

nums = []
isMul = True
res = 0
for i in range(len(lines[0])):
    num = 0
    only_ws = True
    for j in range(len(lines)):
        if lines[j][i] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
            num = num * 10 + int(lines[j][i])
            only_ws = False
        elif lines[j][i] == "*":
            isMul = True
            only_ws = False
        elif lines[j][i] == "+":
            isMul = False
            only_ws = False
    if only_ws:
        if isMul:
            prod = 1
            for n in nums:
                prod *= n
            res += prod
        else:
            summa = 0
            for n in nums:
                summa += n
            res += summa
        nums = []
    else:
        nums.append(num)

print(res)


