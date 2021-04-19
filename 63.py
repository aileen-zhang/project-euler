# powerful digit counts

import time
start_time = time.time()

n_powers = 0
max = 1

while pow(9, max) > pow(10, max - 1):
    max += 1

for n in range(2, 10):
    p = 0
    while pow(n, p) < pow(10, max):
        if len(str(pow(n, p))) == p:
            n_powers += 1
        p += 1

# to account for 1^1
print(n_powers + 1) # 49
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 0.573 ms
