def generate_primes(end):
    """ Funciton that calculates primes until the end
    number and returns a list of these primes """
    primes_list = [2, 3]
    for n in range(3, end, 2):
        for prime in primes_list:
            if n % prime == 0:
                break
        else: primes_list.append(n)
    return primes_list

def factorize(num2factor, primes_list):
    for prime in primes_list:
        if num2factor % prime == 0:
            return prime, int(num2factor / prime)
            

def prime_factorizator(num2factor, highest_exp_factor):
    # generates a prime list until a given number
    primes = generate_primes(highest_exp_factor)

    # finding a factor of the number to factorize
    factors = []

    while True:
        if num2factor not in primes:
            print(f"{num2factor} can be divided by")
            factor, num2factor = factorize(num2factor, primes)
            factors.append(factor)
            print(f"{factor} to give {num2factor}\n")
        else:
            factors.append(factor)
            break

prime_factorizator(600851475143, 100_000)
