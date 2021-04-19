# first Fibonacci number with > n digits

import time
start_time = time.time()

n = 1000
fib = [1, 1]
i = 0

while len(str(fib[-1])) < n:
    fib.append(fib[i] + fib[i + 1])
    i += 1

print(len(fib)) # 4782
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 32.926 ms
