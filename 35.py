# circular primes below 1000000

import itertools

n = 1000000
digits = [1, 3, 7, 9]

# generate all possible digit combos between 3 and 6 digits long

candidates = []

for r in range(3, 7):
    tuples = itertools.product(digits, repeat=r)
    for number in tuples:
        num = 0
        for i, digit in enumerate(number):
            num += digit * pow(10, i)
        candidates.append(num)

# list of primes less than 1000000

primes = [True] * n
primes[0] = primes[1] = False

for i, p in enumerate(primes):
    if p:
        for c in range(i*i, n, i):
                primes[c] = False

prime_candidates = []

for c in candidates:
    if primes[c] == True:
        prime_candidates.append(c)

i = 0
while i < 10: # why does it take 10 loops through to get them all?
    for p, prime in enumerate(prime_candidates):
        next = int(str(prime)[1:] + str(prime)[0])
        if next not in prime_candidates:
            prime_candidates.pop(p)
    i += 1

print(len(prime_candidates) + 13) # include the 13 less than 100
