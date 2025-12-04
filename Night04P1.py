import sys

accessible = 0
grid = []

# obtain input
for line in sys.stdin:
    grid.append([x for x in line.strip("\n").strip("\r")])

grid_h = len(grid)
grid_w = len(grid[0])

for i in range(grid_h):
    for j in range(grid_w):
        if grid[i][j] == "@":
            # Check for less than 4
            blocked_spaces = 0
            if j + 1 < grid_w and grid[i][j + 1] == "@":
                blocked_spaces += 1
            if j + 1 < grid_w and i + 1 < grid_h and grid[i + 1][j + 1] == "@":
                blocked_spaces += 1
            if j + 1 < grid_w and i > 0 and grid[i - 1][j + 1] == "@":
                blocked_spaces += 1
            if j > 0 and grid[i][j - 1] == "@":
                blocked_spaces += 1
            if j > 0 and i + 1 < grid_h and grid[i + 1][j - 1] == "@":
                blocked_spaces += 1
            if j > 0 and i > 0 and grid[i - 1][j - 1] == "@":
                blocked_spaces += 1
            if i + 1 < grid_h and grid[i+1][j] == "@":
                blocked_spaces += 1
            if i > 0 and grid[i-1][j] == "@":
                blocked_spaces += 1

            if blocked_spaces < 4:
                accessible += 1
print(accessible)
            
            

