# taxicab paths

import math
grid_size = 3

paths = math.factorial(2 * grid_size) / math.factorial(grid_size) ** 2

print(paths)
