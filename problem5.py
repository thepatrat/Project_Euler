
checked_numbers = []
number_list = [11, 13, 14, 16, 17, 18, 19, 20]

def is_evenly_divisible(number):
    for i in number_list:
        if number % i != 0:
            return False
    else:
        return True

def find_trivial_solution(min_num, max_num):
    product = min_num
    for i in range(min_num + 1, max_num + 1):
        product = i * product
    return product

def check_numbers(start_number):
    Active = True
    number = start_number

    while Active:    
        if not (is_evenly_divisible(number)):
            # we add 20 because it has to be devisibly by 20
            number += 20
        else:
            return number

number = check_numbers(232792500)
print(number)
# 232792560

print(is_evenly_divisible(232792560))