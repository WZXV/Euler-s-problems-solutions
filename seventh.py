def is_prime(number):
    for num in range(2, round(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True


res = []
i = 2
while len(res) < 10_001:
    if is_prime(i):
        res.append(i)
    i += 1
print(res[-1])