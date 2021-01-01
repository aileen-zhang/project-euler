# largest product of n consecutive numbers in a sequence

file = open("8.txt", "r")
input = ''
for line in file:
    input += line.strip("\n")

n = 13
products = []
i = 0
p = 1

while i < n:
    p *= int(input[i])
    i += 1

while i < len(input) - n:
    j = 0
    p = 1
    while j < n:
        p *= int(input[i + j])
        j += 1
    products.append(p)
    i += 1

products.sort()
print(products[-1])
