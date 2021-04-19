# sum of long-ass list of numbers

import time
start_time = time.time()

input = open("13.txt", "r")
sum = 0

for line in input:
    num = int(line)
    sum += num

print(str(sum)[:10]) # 5537376230
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 3.192 ms

input.close()
