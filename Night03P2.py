import sys
sum = 0
digits_left = 12


for line in sys.stdin:
    line = line.strip('\n').strip('\r')
    cur_sum = 0
    last_i = 0
    j = digits_left
    while (j > 0):
        
        biggest_d = 0
        biggest_i = -1
        if (j > 1):
            search = line[last_i:-1 * (j - 1)]
        else:
            search = line[last_i:]
        for c in enumerate(search, last_i):
            if int(c[1]) > biggest_d:
                biggest_i = c[0]
                biggest_d = int(c[1])   
        last_i = biggest_i + 1
        cur_sum = cur_sum * 10 + biggest_d
        j -= 1
    sum += cur_sum

print(sum)

