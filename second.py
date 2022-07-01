numbers = {}
res = 0

def fib(n):
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in numbers:
        numbers[n] = fib(n - 1) + fib(n -2)

    return numbers[n]

def check():
    global res

    n = 1
    k = 1
    while k < 4_000_000:
        if k % 2 == 0:
            res += k
        n += 1
        k = fib(n)
check()
print(res)
