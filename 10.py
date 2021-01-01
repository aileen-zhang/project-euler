# sum of primes below n

n = 2000000
primes = [True] * n
primes[0] = primes[1] = False
sum = 0

for i, p in enumerate(primes):
    if p:
        for c in range(i*i, n, i):
                primes[c] = False
        sum += i

print(sum)
