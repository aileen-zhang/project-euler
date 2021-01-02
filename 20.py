# sum of digits in factorial

f = 1
for n in range(1, 101):
    f *= n

s = str(f)
sum = 0
for d in s:
    sum += int(d)

print(sum)
