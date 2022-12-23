
# Daylan Stoica

# @DaylanDStoica

'''
Investigating a Prime Pattern
Problem 146

The smallest positive integer n for which the numbers 
n**2+1, n**2+3, n**2+7, n**2+9, n**2+13, and n**2+27 
are consecutive primes is 10. The sum of all such integers n below one-million is 1242490.

What is the sum of all such integers n below 150 million?
'''

from shared_math import is_prime
def check_for_consec_primes( num1, num2):
    '''check that the given numbers are simultaneously:
    1. primes
    2. consecutive primes'''
    result = True 
    if ( not is_prime(num1) ) or ( not is_prime(num2) ):
        # if either of the given numbers are not primes, they cannot be consecutive primes
        # immediately return False
        result = False 
        return result 
    
    # print( num1, " and ", num2, " are both prime numbers. \n Checking if they are consecutive primes...")
    for x in range ( num1+2, num2, 2):
        #check all numbers between the two numbers, confirmed primes
        # because, with the reasoning of all primes are odd, except two, can increment by 2
        # for the same logic, begin the search +2 above the lower number
        if is_prime(x):
            # if there is a prime integer between the two given prime integers
            # return False
            # print( x ," is a prime number between: ", num1, " and " , num2)
            # print( num1, " and " , num2, " are not consecutive primes")
            result = False
            return result 
            break 
        else:
            continue
    
    return result

def check_integer(num):
    '''check if the given integer passes the conditions:
    n**2+1, n**2+3, n**2+7, n**2+9, n**2+13, and n**2+27
    are each consecutive primes
    '''
    result = True 
    
    sq_num = num * num 
    primes_list = [ sq_num + 1, sq_num + 3, sq_num + 7, sq_num + 9, sq_num + 13, sq_num + 27]
    # the list of primes to be checked if they are consecutive
    
    # for num1 in primes_list[:-1], num2 in primes_list[1:]:
        # compare the two numbers, going from the 
    for x in range( len(primes_list)-1 ):
        # check each index in the primes_list, and the next index for consecutively prime
        if check_for_consec_primes( primes_list[x], primes_list[x+1]):
            continue 
        else:
            result = False 
            break
    return result 

def test_base_case ():
    for x in range( 1,11):
        if check_integer(x):
            print(x, " passes the conditions") # 10 should be the only one that passes
        else:
            print( x, " does not pass the conditions")
            
            
# test_base_case()

def sum_the_candidates( num_list):
    ''' given the list of valid integers, sum the contents'''
    sum = 0
    for x in num_list:
        sum += x 
    return sum 


def driver_function():
    '''the body of execution'''
    candidate_list = []
    print( "going up to 15,000,000")
    for x in range(3, 15000000): 
        # from 3 to 15 million, 
        if check_integer(x):
            print(x, " is a valid integer, adding to the list")
            candidate_list.append(x) 
        elif x % 1000 == 0:
            # occassionally give status of the process
            print("reached ", x)
    print(" 15,000,000 reached")
    print("Candadate list")
    print( candidate_list)
    sum = sum_the_candidates(candidate_list)
    print( "sum of the candidates: ", sum)
    
    

def main():
    driver_function()
    
main()