# sieve method:
import math
from datetime import datetime
from tqdm import tqdm

startTime = datetime.now()

def _generate_list(max_number):
    """ Creates a list of integers from 1 to the given number """
    integers_to_n = [2]
    for i in range(3, max_number + 1, 2):
        integers_to_n.append(i)
    return integers_to_n

def sieving(integer_list):
    """ Uses the eukledian prime sieving method to delete non primes from 
    a list of integers """

    # find the end number
    end_number = int(math.sqrt(integer_list[-1]))
    # loop that provides the numbers, of which we are deleting the 
    # multiples.
        # tqdm shows us a progress bar of the loop
    for number in tqdm(range(3, end_number)):
        # only runs it if the number has not yet been deleted from our integer list
        # therefore only checks for the remaining numbers ( = primes)
        if number in integer_list:
            # checks if the elements in the integer list can be divided by the 
            # integer and if they can it deletes them
            for n in integer_list:
                if n % number == 0 and n != number: 
                    integer_list.remove(n)
        else:
            # if the number was already deleted it passes and goes to the next
            pass
        # now it runs again over the shortened list
    return integer_list

# creates our prime list until the max number
max_number = 2_000_000
prime_list = sieving(_generate_list(max_number))

# gives the results
print(f"\n\nWe found {len(prime_list)} primes. The sum over these primes "
    f"is {sum(prime_list)}.")
print(f"The caluclation took {datetime.now() - startTime} minutes.")
