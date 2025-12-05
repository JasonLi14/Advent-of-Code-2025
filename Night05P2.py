import sys

fresh = 0 
pairs = []

for line in sys.stdin:
    l = line.strip("\n").strip("\r")

    if (l == ""):
        break
    
    l = l.split("-")
    lower = int(l[0])
    higher = int(l[1])

    pairs.append((lower, higher))

# Sort pairs
pairs.sort()
merged_pairs = []

for p in pairs:
    should_append = True
    for q in merged_pairs:
        if q[1] >= p[0]:
            q[1] = max(p[1], q[1])
            should_append = False
            break
    if should_append:
        merged_pairs.append([p[0], p[1]])
    
print(merged_pairs)

for p in merged_pairs:
    fresh += p[1] - p[0] + 1

print(fresh)
  
