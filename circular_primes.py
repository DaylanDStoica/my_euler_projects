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
def string_permutations( num):
    '''create the different permutations of a string's characters
    return list of the different ways the chars can be ordered'''
    str_num = str(num)
    # perm_list = [ str_num]

    # cycle through what the different permutations can be
    # startint with moving around the first index, and what can changed in the forward indices
    # and move forward from there.
    # digit_list = str_num.break()
    # digit_list = split( str_num)
    
    # digit_list = list(str_num)
    
    # perm_list = itertools.permutations( digit_list, len(digit_list) )
    perm_list = itertools.permutations(str_num) # automatically separates the chars into permutes
    #get all the permutations, that are of the length of the original number
    #AKA, rearrange the numbers, without dropping or replicating any digits
    
    # test the function, with the perm_list, and using iterations package.
    # Test successfult
    # print(digit_list)
    # print(str_num)
    # print(perm_list)
    
    # for p in perm_list:
        # print(p)
        # p.join()
    return perm_list # returns the list of permutations, without joining the chars into a real integer

    
# string_permutations(123)

def check_rotation_prime(number):
    print("checking the rotation primes of " , number)
    circled_list = string_permutations(number)
    p1 = ''
    for p in circled_list:
        # p1.append(p)
        # p1.append( " ")
        # print(p) # ('1',)
        p1 += p 
        p1 += " "
        # TODO: join the sub-tuples into integers
        # circled_list is currently a nested-list
    # print(" the permutations are: ", circled_list)
    print(" the permutations are: ", p1)
    
    # go through the list of questioned integer ordering
    # checking for prime, then checking that the when the order is changed, 
    # is still a prime
    result = True 
    """
    for num1 in circled_list:
        # str_num1 = string(num1)
        if is_prime( int(num1) ):
        # if is_prime( num1):
            continue 
        else:
            result = False 
            break 
    return result 
    """
    for str_num1 in circled_list:
        # str_num1.join()
        # str2 = list( map( "".join, str_num1) )
        if is_prime( int(str_num1) ):
        # if is_prime( int ( str2) ):
            continue 
        else:
            result = False 
            break 
    return result

def main():
    ''' count the circular primes less than 1 million'''
    upper_limit = 10**6 # 1 million 1,000,000

    count_circ_primes = 0
    for x in range(1, upper_limit): # up to less than 1 million
        if check_rotation_prime(x):
            count_circ_primes += 1
            print( x , " is a circular prime")
    print( count_circ_primes, " is the count of circular primes")

main()