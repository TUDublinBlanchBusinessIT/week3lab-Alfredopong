# Alfred Ukpong
# 17/02/25
# divisors.py.

def divisors(num):
    result = []
    
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    
    return result

print(divisors(30))  
