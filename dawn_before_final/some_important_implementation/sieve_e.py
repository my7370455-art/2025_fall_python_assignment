def sieve_of_eratosthenes(limit):
    # Create a boolean array "prime[0..limit]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    p = 2
    while (p * p <= limit):
        # If primes[p] is not changed, then it is a prime
        if primes[p] == True:
            # Update all multiples of p starting from p*p
            # We start at p*p because smaller multiples 
            # have already been marked by smaller primes
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1

    # Extract the prime numbers from the boolean list
    return [num for num, is_prime in enumerate(primes) if is_prime]

# Example usage:
print(sieve_of_eratosthenes(30))
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]