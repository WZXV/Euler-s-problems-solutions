def check_divided(number):
    for n in range(1, 21):
        if number % n != 0:
            return False
    return True


i = 2520
while not(check_divided(i)):
    i += 20
print(i)