# difference of sum of square and square of sum

n = 100
i = 0
sum = 0
sum_sq = 0
sq_sum = 0

while i <= n:
    sum_sq += i ** 2
    sum += i
    i += 1

sq_sum = sum ** 2

print(sq_sum - sum_sq)
