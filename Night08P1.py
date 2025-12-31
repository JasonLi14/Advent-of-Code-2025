import sys

num_pairs = 1000

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

# Make a dictionary for edges
connections = {}

for pair in distances[:num_pairs]:
    visited[pair[0]] = False
    visited[pair[1]] = False
    if not pair[0] in connections:
        connections[pair[0]] = []
    if not pair[1] in connections:
        connections[pair[1]] = []
    connections[pair[0]].append(pair[1])
    connections[pair[1]].append(pair[0])

# Now, connect the closest pairs 
cycles = []

cur_i = 0
for node in visited:
    if not visited[node]:
        cycles.append([node])
        # Find all nodes which are connected to it
        visit_next = [node]
        while len(visit_next) > 0:
            next_node = visit_next[0]
            if not visited[next_node]:
                visit_next += connections[next_node]
                cycles[cur_i].append(next_node)
            visited[next_node] = True
            visit_next.pop(0)
        cycles[cur_i].pop(0)
        cur_i += 1
cycles.sort(reverse = True, key = lambda x: len(x))
print(len(cycles[0]) * len(cycles[1]) * len(cycles[2]))
