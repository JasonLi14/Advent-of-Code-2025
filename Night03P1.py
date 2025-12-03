import sys
sum = 0

for line in sys.stdin:
    line = line.strip('\n').strip('\r')
    # Get the second biggest digit
    biggest_d = 0
    biggest_i = -1
    for c in enumerate(line[:-1], 0):
        if int(c[1]) > biggest_d:
            biggest_i = c[0]
            biggest_d = int(c[1])    # find the biggest digit after our biggest
    second_d = 0
    for c in enumerate(line[biggest_i+1:], biggest_i + 1):
        if int(c[1]) > second_d:
            second_d = int(c[1])
    sum += biggest_d * 10 + second_d

print(sum)
    
