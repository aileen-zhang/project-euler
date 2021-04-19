# largest product in a square grid

import numpy as np
import time
start_time = time.time()

input = open("11.txt", "r")
arr_in = []

for line in input:
    row = []
    numbers = line.split()
    for number in numbers:
        row.append(int(number))
    arr_in.append(row)

n = len(arr_in)
products = []

def consecutive_row_sum(arr):
    for i, row in enumerate(arr):
        for j, num in enumerate(row[:-3]):
            prod = num * row[j+1] * row[j+2] * row[j+3]
            products.append(prod)

grid = np.array(arr_in)
consecutive_row_sum(grid)

grid = np.transpose(grid)
consecutive_row_sum(grid)

offset1 = np.zeros((n, 2 * n - 1))
for i, row in enumerate(grid):
    for j, num in enumerate(row):
        offset1[i][i + j] = num

offset1 = np.transpose(offset1)
consecutive_row_sum(offset1)

offset2 = np.zeros((n, 2 * n - 1))
for i, row in enumerate(grid):
    for j, num in enumerate(row[::-1]):
        offset2[i][i + j] = num

offset2 = np.transpose(offset2)
consecutive_row_sum(offset2)

products.sort()

print(int(products[-1])) # 70600674
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 7.253 ms

input.close()
