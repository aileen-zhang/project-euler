# sum of long-ass list of numbers

input = open("13.txt", "r")
sum = 0

for line in input:
    num = int(line)
    sum += num

print(sum)
