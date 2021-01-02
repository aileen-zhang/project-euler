# first Fibonacci number with > n digits

n = 1000

fib = [1, 1]
i = 0

while len(str(fib[-1])) < n:
    fib.append(fib[i] + fib[i + 1])
    i += 1

print(len(fib))
