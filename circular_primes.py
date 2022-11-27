# Daylan Stoica
# @DaylanDStoica

# 24 August 2022

'''
Circular primes


Project Eueler
Problem 35

The number, 197, is called a circular prime because all 
rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 
13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from shared_math import is_prime 

import itertools #for getting the permutations
def string_permuations( num):
    '''create the different permutations of a string's characters
    return list of the different ways the chars can be ordered'''
    str_num = str(num)
    perm_list = [ str_num]

    # cycle through what the different permutations can be
    # startint with moving around the first index, and what can changed in the forward indices
    # and move forward from there.
    # digit_list = str_num.break()
    # digit_list = split( str_num)
    digit_list = list(str_num)
    
    per_list = itertools.permutations( digit_list, len(digit_list) )
    #get all the permutations, that are of the length of the original number
    #AKA, rearrange the numbers, without dropping or replicating any digits
    
    # TODO: test the function, with the perm_list, and using iterations package.
    
    return perm_list
    
def check_rotation_prime(number):
    circled_list = string_permuations(number)
    # go through the list of questioned integer ordering
    # checking for prime, then checking that the when the order is changed, 
    # is still a prime
    result = True 
    for num1 in circled_list:
        if is_prime( int(num1) ):
            continue 
        else:
            result = False 
            break 
    return result 
