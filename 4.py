# largest palindrome from product of two three-digit numbers

max = 999
i1 = 1
palindromes = []

while i1 < max:
    i2 = 1
    while i2 < max:
        num = i1 * i2
        if str(num) == str(num)[::-1]:
            palindromes.append(num)
        i2 += 1
    i1 += 1

palindromes.sort()
print(palindromes[-1])
