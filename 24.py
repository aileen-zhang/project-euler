# lexigraphical permutations... this feels like cheating

from itertools import permutations

print(list(permutations(range(10)))[1000000 - 1])
