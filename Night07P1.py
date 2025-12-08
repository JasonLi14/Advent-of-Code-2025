import sys

lines = []
for line in sys.stdin:
    lines.append([x for x in line.strip("\n").strip("\r")])

splits = 0

for i in range(1, len(lines)):
    for j in range(0, len(lines[i])):
        if lines[i][j] == ".":
            if lines[i-1][j] == "S":
                lines[i][j] = "|"
            elif lines[i-1][j] == "|":
                lines[i][j] = "|"
        elif lines[i][j] == "^":
            if lines[i-1][j] == "|":
                splits += 1
                if j > 0:
                    lines[i][j-1] = "|"
                if j + 1 < len(lines[i]):
                    lines[i][j+1] = "|"
print(splits)
        
        
