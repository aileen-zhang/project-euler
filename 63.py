# powerful digit counts

n_powers = 0
max = 1
while pow(9, max) > pow(10, max - 1):
    max += 1

for n in range(2, 10):
    p = 0
    while pow(n, p) < pow(10, max):
        if len(str(pow(n, p))) == p:
            n_powers += 1
            # print(n, p, pow(n, p))
        p += 1

print(n_powers + 1) # for 1^1
