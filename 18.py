# maximum path sum (problems 18 and 67)

file = open("67.txt", "r")
arr = []

for line in file:
    row = []
    numbers = line.split()
    for number in numbers:
        row.append(int(number))
    arr.append(row)

while len(arr) > 1:
    this = arr[-2]
    next = arr[-1]
    for i, n in enumerate(this):
        left = next[i]
        right = next[i + 1]
        this[i] = n + max(left, right)
        arr[-2] = this
    arr.pop()

print(arr)

file.close()
