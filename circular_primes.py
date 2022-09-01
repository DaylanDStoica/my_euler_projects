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

def string_permuations( num):
    '''create the different permutations of a string's characters
    return list of the different ways the chars can be ordered'''
    str_num = str(num)
    perm_list = [ str_num]

    return perm_list
    
def check_rotation_prime(number):
    circled_list = string_permuations(number)
    # go through the list of questioned integer ordering
    # checking for prime
    result = True 
    for num1 in circled_list:
        if is_prime( int(num1) ):
            continue 
        else:
            result = False 
            break 
    return result 