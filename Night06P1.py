import sys

lines = []
for line in sys.stdin:
    l = list(filter(None, line.strip("\n").strip("\r").split(" ")))
    lines.append(l)

res = 0
for i in range(len(lines[0])):
    if lines[-1][i] == "+":
        summa = 0
        for j in range(len(lines) - 1):
            summa += int(lines[j][i])
        res += summa
    else:
        prod = 1
        for j in range(len(lines) - 1):
            prod *= int(lines[j][i])
        res += prod
print(res)
    


