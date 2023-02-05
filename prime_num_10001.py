# Daylan Stoica
# @DaylanDStoica

# 4 Februrary 2023

'''
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from shared_math import is_prime

def find_the_xth_prime ( limit = 100):
    ''' find the count-th prime number'''

    #starting at 3, already counting 2 as a prime 
    counter = 1 # count the number of prime-numbers encountered
    num = 3
    while counter < limit:
        #loop until the number of primes is reached. Print each new prime and count 
        if is_prime(num):
            counter += 1 
            print( "new prime: ", num, "prime count: ", counter)
        num += 2 # increment to skip the evens.


find_the_xth_prime()