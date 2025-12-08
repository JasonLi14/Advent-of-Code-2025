import sys

lines = []
for line in sys.stdin:
    lines.append([x for x in line.strip("\n").strip("\r")])

splits = 0

possibs_grid = [[0 for x in lines[0]] for y in lines]
possibs_grid[len(lines) - 1] = [1 for i in lines[0]]

for i in range(len(lines) - 2, -1, -1):
    for j in range(len(lines[i])):
        if lines[i][j] == "^":
            possibs_grid[i][j] = 0
            if j > 0:
                possibs_grid[i][j] += possibs_grid[i+1][j - 1]
            if j + 1 < len(lines[i]):
                possibs_grid[i][j] += possibs_grid[i+1][j + 1]
        elif lines[i][j] == ".":
            possibs_grid[i][j] = possibs_grid[i+1][j]
        elif lines[i][j] == "S":
            print(possibs_grid[i + 1][j])
        
