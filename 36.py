# sum of palindromes in base 10 and 2 less than one million
# too lazy to deal with leading 0s when generating palindromes

import time
start_time = time.time()

def check_palindrome(s):
    l = len(s) - 1
    for i, d in enumerate(s):
        if d != s[l - i]:
            return False
    return True

candidates = list(range(1, 1000000, 2))
base10_palindromes = []
total = 0

for c in candidates:
    if check_palindrome(str(c)):
        base10_palindromes.append(c)

for p in base10_palindromes:
    if check_palindrome(bin(p)[2:]):
        total += p

print(total) # 872187
print("%.3f ms" % ((time.time() - start_time) * 1000)) # 280.192 ms
