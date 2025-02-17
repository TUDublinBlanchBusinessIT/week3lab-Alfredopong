# Alfred Ukpong
# 17/02/25
# divisors.py.

from divisors import divisors

def isPerfectNumber(n):
    if sum(divisors(n)) - n == n:
        return True
    return False

count = 0
num = 1

while count < 4:
    if isPerfectNumber(num):
        print(num, "is a perfect number")
        count += 1
    num += 1
