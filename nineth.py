
for biggest in range(1, 500):
    for bigger in range(1, biggest):
        for num in range(1, bigger):
            if bigger ** 2 + num ** 2 == biggest ** 2 and num + bigger + biggest == 1000:
                print(num * bigger * biggest)
                exit()