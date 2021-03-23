start_num = 0
end_num = 10

def sum_of_squares(start_num, end_num):
    sum_of_squares = 0
    for i in range(start_num, end_num + 1):
        sum_of_squares += i ** 2
    return sum_of_squares

def square_of_sum(start_num, end_num):
    sum_numbers = 0
    for i in range(start_num, end_num + 1):
        sum_numbers += i
    square_of_sum = sum_numbers ** 2
    return square_of_sum


print(square_of_sum(1, 100))

print(sum_of_squares(1, 100))

print(square_of_sum(1, 100) - sum_of_squares(1, 100))

# 25164150