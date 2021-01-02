# highly divisible triangular number with more than f factors

import numpy as np
f = 500

def triangle(n):
    return n * (n + 1) / 2

def factor_count(n):
    factors = {2:0}
    while n % 2 == 0:
        n /= 2
        factors[2] += 1
    for prime in range(3, int(np.floor(np.sqrt(n + 1))), 2):
        factors[prime] = 0
        while n % prime == 0:
            n /= prime
            factors[prime] += 1
    if n != 1:
        factors[n] = 1
    sum = 1
    for f in factors:
        sum *= (factors[f] + 1)
    return sum

n = 1
while factor_count(triangle(n)) < f:
    n += 1

print(triangle(n))
