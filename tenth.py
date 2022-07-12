from math import sqrt, ceil


def is_prime(n):
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

res = 2

for n in range(3, 2_000_000, 2git ):
    if is_prime(n):
        res += n
print(res)