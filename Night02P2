import math
inp = input().split(",")
inp = [i.split("-") for i in inp]
the_sum = 0
print(inp)
for i in inp:
    for j in range(int(i[0]), int(i[1]) + 1):
        str_j = str(j)
        digs = len(str_j)
        # Go through divisors of digs
        for n in range(2, digs + 1):
            if (digs % n == 0):
                incre = digs // n
                seed = str_j[:incre]
                passed = True
                for k in range(n):
                    if str_j[incre * k:incre * (k + 1)] != seed:
                        passed = False
                        break
                if passed == True:
                    the_sum += j
                    break
        
print(the_sum)
