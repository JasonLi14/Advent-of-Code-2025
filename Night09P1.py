import sys

reds = []

# Get input
for line in sys.stdin:
    x, y = (int(x) for x in line.split(","))
    reds.append((x,y))

biggest = 0
for i in range(len(reds)):
    for j in range(len(reds) - 1):
        biggest = max(biggest,
            abs(reds[j][0] - reds[i][0] + 1) * abs(reds[j][1] - reds[i][1] + 1))

print(biggest)
