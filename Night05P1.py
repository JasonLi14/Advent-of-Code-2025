import sys

fresh = 0 
pairs = []

for line in sys.stdin:
    l = line.strip("\n").strip("\r")

    if (l == ""):
        break
    
    l = l.split("-")
    pairs.append((int(l[0]), int(l[1])))

for line in sys.stdin:
    l = line.strip("\n").strip("\r")     
    n = int(l)
    for p in pairs:
        if p[0] <= n and n <= p[1]:
            fresh += 1
            break

print(fresh)
