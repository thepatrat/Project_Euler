# Reading in the number into a str
with open("files/problem8.txt", "r") as f:
    num_1000_digits = ""
    for line in f:
        line = f.readline().rstrip()
        num_1000_digits = num_1000_digits + line

def _make_digit_string(num_str, number_of_digits, position):
    # creating a x digit string from the current position
    digit_str = ""
    for i in range(number_of_digits):
        digit_str = digit_str + num_str[position + i]
    return digit_str

def _make_product_of_digits(digit_str):
    product = 1
    for i in digit_str:
        product = product * int(i)
    return product

def _non_zero(digit_str):
    for i in digit_str:
        if int(i) == 0:
            return False
    else:
        return True

def find_highest_product(num_1000_digits, number_of_digits):
    highest_product = 0
    # iterates over the positions in the number
    for i in range(len(num_1000_digits)- number_of_digits):
        # creates a string from the number with the length
        # given in number of digits at the position i
        temp_str = _make_digit_string(num_1000_digits, number_of_digits, i)
        
        # checks if the string contains a zero
        if _non_zero(temp_str):
            temp_product = _make_product_of_digits(temp_str)
            
            # checks if the product is higher than previous ones
            if temp_product > highest_product:
                # if yes it sets the new highest product and saves the
                # corresponding digits and position
                highest_product = temp_product
                digits = temp_str
                position = i
            else:
                pass
        else:
            pass

    return highest_product, digits, position


results = find_highest_product(num_1000_digits, 13)
print(f"The highest product is {results[0]}, "
    f"which is the product of {results[1]}, "
    f"which we can find at position {results[2]}")