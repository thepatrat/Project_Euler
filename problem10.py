# sieve method:
import math
from datetime import datetime
from tqdm import tqdm

startTime = datetime.now()

def _index_is_value_list_gen(max_number):
    """ Creates a list of integers from 0 to the given number.
    The index of the list correspond to the value."""
    integers_to_n = []
    for i in range(0, max_number + 1, 1):
        integers_to_n.append(i)
    return integers_to_n

def _zero_all_multiples(integer_list, number):
    """ Sets all the multiples of a number from a list 
    of integers to zero, integer list must start from 0 """
    # checks what the maximum number in the list is
    highest_number = max(integer_list)
    # we start with a multiple of 2 for each number
    # otherwise the original number is deleted
    n = 2
    # the multiple of the number cant exceede the maximum number
    while n * number <= highest_number:
        # sets the value of the n times multiple to 0,
        # faster method than checking the list for a given value
        integer_list[n * number] = 0
        # we go to the next multiple of the number
        n += 1
    # returns a list with multiple set to zero
    return integer_list

def _delete_values_from_list(integer_list, value):
    # list comprehension, fancy for-loop
    integer_list = [i for i in integer_list if i != value]
    return integer_list

def _sieving(integer_list):
    # create a list to store our primes in
    primes = []
    # we only have to run the check until highest number ** 0.5
    max_number = int(math.sqrt(integer_list[-1]))
    # repeat the elimination prozess until current number
    # is the square root of the max number
        # tqdm is used to give us a loading bar over this loop
    for new_prime in tqdm(range(2, max_number)):    
        # only checks the lowest number not in the prime list, when the value of it is non zero
        if new_prime not in primes and integer_list[new_prime] != 0:
            # this number must be a prime, so zero all the multiples 
            # of it in our integer list, so they are not checked in the next run
            integer_list = _zero_all_multiples(integer_list, new_prime)
    # deletes all 0s (non primes) from the list and then adds the remaining values to the primes list
    primes = _delete_values_from_list(integer_list, 0)[1:]
    # returns the list we stored the primes in
    return primes


# creates our prime list until the max number and use the sieving method on
max_number = 10_000_000
prime_list = _sieving(_index_is_value_list_gen(max_number))

# gives the results
print(f"\n\nWe found {len(prime_list)} primes. The sum over these primes "
     f"is {sum(prime_list)}.")
print(f"The caluclation took {datetime.now() - startTime}.")

# times
# 10: 20.4 ms
# 100: 15.4 ms
# 1000: 15.4 ms
# 10_000: 26 ms
# 100_000: 240 ms
# 1_000_000: 3339 ms
# 2_000_000: 7160 ms
# 10_000_000: 4978.4 ms
#
# What did i learn:
#   checking a list for values is way slower to zero that value, use the index instead (if known)
#   in this case the index corresponds to the value in the list
#
#   dont brute force it, method works because it is not checking if the number is dvivisible by the primes before
#   it eliminates numbers from a pool of possible primes by eliminiating multiples of all previous primes
#   therefore it only checks if the number was eliminated 
#   (in this case the value corresponding to the number as an index is non zero)
#
#   drastic performance by only checking primes to be multiplied until the square root
#   of our limit / the max integer in the list