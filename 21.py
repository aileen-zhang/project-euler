# amicable numbers less than 10000

max = 10000

divisor_sums = [0]

for n in range(1, max):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    divisor_sums.append(sum)

amicable_sum = 0

for value, sum in enumerate(divisor_sums):
    if sum < max:
        if divisor_sums[sum] == value and sum != value:
            amicable_sum += value

print(amicable_sum)
