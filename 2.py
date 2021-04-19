# sum of even Fibonacci numbers

import time
start_time = time.time()

max = 4000000
fib = [1, 1]
i = 0
sum = 0

while fib[-1] < max:
    fib.append(fib[i] + fib[i + 1])
    i += 1

for num in fib:
    if num % 2 == 0:
        sum += num

print(sum) # 4613732
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 0.079 ms
