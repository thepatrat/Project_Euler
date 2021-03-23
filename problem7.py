def generate_primes(number_of_primes):
    """ Funciton that calculates primes until the end
    number and returns a list of these primes """
    primes_list = [2, 3]
    number = 3
    while number_of_primes > len(primes_list):
        number += 2
        check_if_prime(number, primes_list)
    return primes_list

def check_if_prime(number_to_check, primes_list):
    """ Function checks if the number_to_check is evenly divisible
    by the primes in the prime list """
    for prime in primes_list:
        if number_to_check % prime == 0:
            break
    else:
        primes_list.append(number_to_check)
    return primes_list

primes_list = generate_primes(10_001)
print(primes_list[-1])

# 104743