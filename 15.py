# taxicab paths

import time
start_time = time.time()

import math
grid_size = 3

paths = math.factorial(2 * grid_size) / math.factorial(grid_size) ** 2

print(int(paths)) # 20
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 0.146 ms
