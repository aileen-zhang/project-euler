# smallest common multiple

max = 20
i = 1
numbers = []
scm = 1

while i <= max:
    numbers.append(i)
    i += 1

for n, num in enumerate(numbers):
    for factor in numbers[:n]:
        if num % factor == 0:
            num /= factor
    numbers[n] = num

for num in numbers:
    scm *= num

print(numbers)
print(scm)
