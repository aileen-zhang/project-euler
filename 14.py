# longest Collatz sequence starting at a value < n

n = 1000000

def collatz_len(x):
    length = 1
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = (3 * x) + 1
        length += 1
    return length

max_len = 0
max_n = 0

for n in range(1, n):
    if collatz_len(n) > max_len:
        max_len = collatz_len(n)
        max_n = n

print(max_n)
