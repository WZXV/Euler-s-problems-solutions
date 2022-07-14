# Slow solution
def is_prime(number):
    for num in range(3, round(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True


def sum_primes_slow(n):
    res = 2

    for i in range(3, n, 2):
        if is_prime(i):
            res += i

    return res


print(sum_primes_slow(2_000_000))


# Fast solution(Sieve of Eratosthenes)
def sum_primes_fast(n):
    res = 0
    primes = [True] * n

    for i in range(2, n):
        if primes[i]:
            res += i
            for j in range(i ** 2, n, i):
                primes[j] = False

    return res


print(sum_primes_fast(2_000_000))