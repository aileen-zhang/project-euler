# naive fraction cancelling

max = 100
numerators = []
denominators = []

for n in range(10, max):
    for m in range(10, n):
        if m % 10 != 0 and n % 10 != 0:
            em, en = str(m), str(n)
            new_m, new_n = 0, 0
            if em[0] == en[0]:
                new_m = int(em[1])
                new_n = int(en[1])
            elif em[0] == en[1]:
                new_m = int(em[1])
                new_n = int(en[0])
            elif em[1] == en[0]:
                new_m = int(em[0])
                new_n = int(en[1])
            elif em[1] == en[1]:
                new_m = int(em[0])
                new_n = int(en[0])
            if new_m != 0 and new_n != 0:
                if m / n == new_m / new_n:
                    numerators.append(m)
                    denominators.append(n)

n_prod = 1
d_prod = 1

for n in numerators:
    n_prod *= n

for d in denominators:
    d_prod *= d

for i in range(1, n_prod + 1):
    if n_prod % i == 0 and d_prod % i == 0:
        gcd = i

print(d_prod / i)
