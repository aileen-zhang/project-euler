# smallest common multiple

import time
start_time = time.time()

max = 20
i = 1
numbers = []
scm = 1

while i <= max:
    numbers.append(i)
    i += 1

for n, num in enumerate(numbers):
    for factor in numbers[:n]:
        if num % factor == 0:
            num /= factor
    numbers[n] = num

for num in numbers:
    scm *= num

print(int(scm)) # 232792560
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 0.138 ms
