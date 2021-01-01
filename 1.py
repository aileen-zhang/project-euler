# sum of multiples of 3 or 5

n = 1000
i = 0
sum = 0
while i < n:
    if i % 3 == 0 or i % 5 == 0:
        sum += i
    i += 1

print(sum)
