# maximum path sum (problems 18 and 67)

import time
start_time = time.time()

file = open("18.txt", "r")
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

print(arr[0][0]) # 1074 / 7273
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 3.576 ms / 6.692 ms

file.close()
