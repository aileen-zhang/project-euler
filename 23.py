# sum of all numbers not expressible as sum of two abundant numbers

import math
import time
start_time = time.time()

max = 28123
divisor_sums = [0] * max
abundant_numbers = []
expressible = []
inexpressible = [True] * max
inexpressible_sum = 0

for n in range(1, max):
    sum = 0
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n / i:
                sum += i
            else:
                sum += (i + n/i)
    divisor_sums[n] = int(sum)

for n, sum in enumerate(divisor_sums):
    if sum > n:
        abundant_numbers.append(n)

for i, n in enumerate(abundant_numbers):
    for j, m in enumerate(abundant_numbers[i:]):
        expressible.append(m + n)
        if (m + n) > max:
            break

expressible.sort()

for i in expressible:
    if i < max:
        inexpressible[i] = False
    else:
        break

for i, b in enumerate(inexpressible):
    if b:
        inexpressible_sum += i

print(inexpressible_sum) # 4179871
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 6475.334 ms
