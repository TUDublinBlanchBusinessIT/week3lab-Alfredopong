# Alfred Ukpong
# 17/02/25
# perfectNumber.py

from divisors import divisors

def perfectNumber(x):
    if sum(divisors(x)) - x == x:
        return True
    return False

if perfectNumber(8128):
    print("8128 is a perfect number")

