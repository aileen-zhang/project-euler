# find Pythagorean triplet that sums to 1000

import numpy as np
a = 0
product = 0

while a < 250:
    b = 250
    while b < 500:
        c = np.sqrt(a ** 2 + b ** 2)
        if c % 1 == 0:
            if a + b + c == 1000:
                triple = (a, b, c)
                product = a * b * c
                break
        b += 1
    if product != 0:
        break
    a += 1

print(triple)
print(product)
