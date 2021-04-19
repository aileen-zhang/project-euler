# sum of digits of 2^n

import time
start_time = time.time()

n = 1000

def digit_sum(x):
    text = str(x)
    sum = 0
    for t in text:
        sum += int(t)
    return sum

print(digit_sum(2 ** n)) # 1366
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 0.159 ms
