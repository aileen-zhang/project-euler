# coin sums to 200p
# this is pretty much the most inefficient solution

values = [200, 100, 50, 20, 10, 5, 2, 1]

def branch_count(target, divisor_lst):
    divisor = divisor_lst[0]
    if divisor == 1:
        return 1
    else:
        branches = 0
        cycles = target // divisor
        for i in range(cycles + 1):
            branches += branch_count(target - i * divisor, divisor_lst[1:])
        return branches

print(branch_count(200, values))
