from tqdm import tqdm

def check_if_palindrome(number):
    number_string = str(number)
    number_length = len(number_string)

    if number_length % 2 == 0:
        check_length = number_length / 2

    if number_length % 2 != 0:
        check_length = number_length / 2 - 0.5

    for i in range(0, int(check_length)):
        check = (number_string[-i -1] == number_string[i])
        if check == False:
            return False
    else:
        return True


def product_generator(start_num, end_num):
    numbers = []
    products = {}

    for i in range(start_num,end_num + 1):
        numbers.append(i)
    numbers.reverse()

    # len_numbers_0 = len(numbers)

    for n_1 in numbers:
        for n_2 in numbers:
            product = n_1 * n_2
            if product not in products:
                products[product] = (f"{n_1}, {n_2}")
        numbers.pop(0)
        # progress = round((1 - (len(numbers)/len_numbers_0)) * 200, 0)
        # print(f"{int(progress)}%")

    return products


def palindroms_in(num_list):
    palindroms = []

    for i in num_list:
        if check_if_palindrome(i):
            palindroms.append(i)
    palindroms.sort(reverse=True)

    return palindroms


def palindrom_program():
    start_num = int(input("Start number: "))
    end_num = int(input("End number: "))

    products = product_generator(start_num, end_num)

    print(
        "Here are all the products of the numbers in the range"
        f"of {start_num} to {end_num}, \nthat are palindroms: ")
    
    for palindroms in palindroms_in(products.keys()):
        print(f"{palindroms} from {products[palindroms]}")


palindrom_program()
