# sum of digits of 2^n

n = 1000

def digit_sum(x):
    text = str(x)
    sum = 0
    for t in text:
        sum += int(t)
    return sum

print(digit_sum(2 ** n))
