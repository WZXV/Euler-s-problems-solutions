from math import sqrt

num = 600851475143


def is_prime(number):
    for n in range(2, round(sqrt(number))):
        if number % n == 0:
            return False
    return True

max_n = 1

for n in range(2, round(sqrt(num))):
    if num % n == 0:
        if is_prime(n):
            if n > max_n:
                max_n = n

        tmp = num // n
        if is_prime(tmp):
            if n > max_n:
                max_n = n
print(max_n)