# lexigraphical permutations... this feels like cheating

import time
start_time = time.time()

from itertools import permutations

print(list(permutations(range(10)))[1000000 - 1]) # 2783915460 (ish)
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 842.556 ms
