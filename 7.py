# find nth prime

n = 10001
primes = []
i = 2

while len(primes) < n:
    primes.append(i)
    for prime in primes[:-1]:
        if primes[-1] % prime == 0:
            primes.pop()
            break
    i += 1

print(primes[-1])
