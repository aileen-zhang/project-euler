# name scorer

import time
start_time = time.time()

file = open("22.txt", "r")

for line in file:
    names = line.split(",")

for i, name in enumerate(names):
    names[i] = name.strip('"')

names.sort()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
values = {}
for i, letter in enumerate(alphabet):
    values[letter] = (i + 1)

def name_value(name):
    value = 0
    for letter in name:
        value += values[letter]
    return value

score = 0
for i, name in enumerate(names):
    score += (i + 1) * name_value(name)

print(score) # 871198282
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 13.404 ms

file.close()
