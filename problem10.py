# sieve method:
import math
from datetime import datetime
from tqdm import tqdm

startTime = datetime.now()

def _generate_list(max_number):
    """ Creates a list of integers from 1 to the given number """
    integers_to_n = []
    for i in range(3, max_number + 1, 2):
        integers_to_n.append(i)
    return integers_to_n

def _remove_multiples(integer_list, number):
    """ Removes all the multiples of a number from a list 
    of integers """
    # checks what the maximum number in the list is
    highest_number = max(integer_list)
    # we start with a multiple of 2 for each number
    n = 2
    # the multiple of the number cant exceede the maximum number
    while n * number <= highest_number:
        print(n*number)
        # we expect an error, as e.g. 6 is already deleted 
        # because it is a multiple of 2
        try:
            integer_list.remove(number * n)
        except:
            pass
        # we go to the next multiple of the number
        n += 1
    return integer_list

def _sieving(integer_list):
    # create a list to store our primes in
    primes = []
    # repeat our multiple removing until our list is empty
    while integer_list:        
        # check lowest number in the list
        lowest_number = integer_list[0]
        # lowest number must be a prime so safe it in the primes list
        primes.append(lowest_number)
        # now remove all the multiples of the lowest number from our integers
        integer_list = _remove_multiples(integer_list, lowest_number)
        # to get a new lowest number, we delete the old one
        # could be put in remove multiples function, but I want to 
        # keep that one only for multiples
        integer_list.remove(lowest_number)
    return primes



# creates our prime list until the max number and use the sieving method on
max_number = 2_000_000
prime_list = _sieving(_generate_list(max_number))

# gives the results
print(f"\n\nWe found {len(prime_list)} primes. The sum over these primes "
    f"is {sum(prime_list)}.")
print(f"The caluclation took {datetime.now() - startTime}.")
