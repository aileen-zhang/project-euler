# Champernowne's constant

const = ''
for i in range(1000000):
    const += str(i)

product = 1
for i in range(0, 7):
    product *= int(const[pow(10, i)])

print(product)
