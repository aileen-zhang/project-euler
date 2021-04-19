# largest product of n consecutive numbers in a sequence

import time
start_time = time.time()

file = open("8.txt", "r")
input = ''
for line in file:
    input += line.strip("\n")

n = 13
products = []
i = 0
p = 1

while i < n:
    p *= int(input[i])
    i += 1

while i < len(input) - n:
    j = 0
    p = 1
    while j < n:
        p *= int(input[i + j])
        j += 1
    products.append(p)
    i += 1

products.sort()
print(products[-1]) # 23514624000
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 9.243 ms

file.close()
