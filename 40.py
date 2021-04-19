# Champernowne's constant

import time
start_time = time.time()

const = ''
for i in range(1000000):
    const += str(i)

product = 1
for i in range(0, 7):
    product *= int(const[pow(10, i)])

print(product) # 210
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 268.369 ms
