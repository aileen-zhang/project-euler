# sum of digits in factorial

import time
start_time = time.time()

f = 1
for n in range(1, 101):
    f *= n

s = str(f)
sum = 0
for d in s:
    sum += int(d)

print(sum) # 648
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 0.139 ms
