# longest Collatz sequence starting at a value < n
# brute-forced, whoops

import time
start_time = time.time()

n = 1000000
max_len = 0
max_n = 0

def collatz_len(x):
    length = 1
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = (3 * x) + 1
        length += 1
    return length

for n in range(int(n / 2), n):
    if collatz_len(n) > max_len:
        max_len = collatz_len(n)
        max_n = n

print(max_n) # 837799
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 13562.962 ms
