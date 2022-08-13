
# Daylan Stoica
# August 12 2022

# EulerProject # 50

''''
Consecutive prime sum

Problem 50

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from math import sqrt
def is_prime(number):
    # check that number is an integer
    if type(number) != int:
        if int(number) == number: #converting into integer is acceptable
            number = int(number)
        else: #number is not an integer
            print(f"cannot check that non-integer {number} is a prime. Assumed False")
            return False

    
    if number == 1:  # 1 is not a prime
        return False
    elif number == 2: # 2 is a prime
        return True
    elif number == 3: 
        return True 

    for x in range(1, math.ceil( sqrt(number) )):
        if x == 1:
            continue
        if number % x == 0: 
            return False


def test_is_prime():
    for x in range( 0, 20):
        print(f" x is a prime: {is_prime(x)}")

test_is_prime()