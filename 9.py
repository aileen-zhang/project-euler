# find Pythagorean triplet that sums to 1000

import numpy as np
import time
start_time = time.time()

product = 0

for a in range (0, 250):
    for b in range (250, 500):
        c = np.sqrt(a ** 2 + b ** 2)
        if c % 1 == 0:
            if a + b + c == 1000:
                triple = (int(a), int(b), int(c))
                product = int(a * b * c)
                break
    if product != 0:
        break

print(triple) # (200, 375, 425)
print(product) # 31875000
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 96.149 ms
