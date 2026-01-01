import sys

boxes = []

# Obtain input
for line in sys.stdin:
    parsed_line = tuple(int(x) for x in line.split(","))
    boxes.append(parsed_line)

# Calculate all pair distances
distances = []
visited = {}
num_boxes = len(boxes)
for i in range(num_boxes):
    for j in range(i + 1, num_boxes):
        d = 0
        d += (boxes[j][0] - boxes[i][0]) ** 2
        d += (boxes[j][1] - boxes[i][1]) ** 2
        d += (boxes[j][2] - boxes[i][2]) ** 2
        d = d ** (1/2)
        distances.append((i, j, d))

# Sort the distances
distances.sort(key = lambda d: d[2])

cycles = [[x] for x in range(num_boxes)]

cur_i = 0
connection = distances[cur_i]
while len(cycles) > 1:
    connection = distances[cur_i]
    # find the two to merge
    anchor_i = -1
    merge_i = -1
    for c in range(len(cycles)):
        if connection[0] in cycles[c]:
            if anchor_i == -1:
                anchor_i = c
            else:
                merge_i = c
                break
        elif connection[1] in cycles[c]:
            if anchor_i == -1:
                anchor_i = c
            else:
                merge_i = c
                break
    if anchor_i != -1 and merge_i != -1:
        cycles[anchor_i] += cycles[merge_i]
        cycles.pop(merge_i)

    cur_i += 1
print(boxes[connection[0]][0] * boxes[connection[1]][0])

