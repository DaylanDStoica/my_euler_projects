# Daylan Stoica

# @DaylanDStoica

# 22 December 2022

'''
Harshad Numbers
Problem 387

A Harshad or Niven number is a number that is divisible by the sum of its digits.
201 is a Harshad number because it is divisible by 3 (the sum of its digits.)
When we truncate the last digit from 201, we get 20, which is a Harshad number.
When we truncate the last digit from 20, we get 2, which is also a Harshad number.

Let's call a Harshad number that, while recursively truncating the last digit, 
always results in a Harshad number a right truncatable Harshad number.

Also:
201/3=67 which is prime.
Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime.
When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable.
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 10^14.
'''


from shared_math import sum_digits
def is_divisible_by_digisum(num):
    result = False 
    digit_sum = sum_digits(num)
    if num % digit_sum == 0:
        # if the sum of the given number's digits, are evenly divivided by the given number, return True 
        result = True 
    return result 

from shared_math import is_prime
def is_strong_harshad(num):
    ''' if the given number is divisible by the digit_sum
    and when divided by the sum results in a prime'''
    if not is_divisible_by_digisum(num): # if the number is not divisible, return False
        return False 
    else:
        digit_sum = sum_digits(num)
        divised_num = num / digit_sum # divided by the sum of digits
        if is_prime(divised_num):
            return True 
    return False
    
def base_case_test():
    sum = 0 
    for x in range(1,10000):
        if is_divisible_by_digisum(x):
            print(x, " is valid")
            sum += x 
    # should return 90619
    print(" sum is: ", sum, " ... should be 90619")
    return sum 

base_case_test()
