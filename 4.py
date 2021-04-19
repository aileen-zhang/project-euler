# largest palindrome from product of two three-digit numbers

import time
start_time = time.time()

max = 1000
palindromes = []

for i1 in range(1, max):
    for i2 in range(i1, max):
        num = i1 * i2
        if str(num) == str(num)[::-1]:
            palindromes.append(num)

palindromes.sort()

print(palindromes[-1]) # 906609
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 291.458 ms
