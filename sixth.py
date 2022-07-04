sum_squares_list = sum(n**2 for n in range(1, 101))
square_of_sum = ((1 + 100) * 100 // 2) ** 2
print(square_of_sum - sum_squares_list)