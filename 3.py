# greatest prime factor of n

n = 600851475143
i = 1

while n != 1:
    if n % i == 0:
        n /= i
    i += 1

print(i - 1)
