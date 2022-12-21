
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

def check_for_consec_primes():
    pass 

def check_integer(num):
    '''check if the given integer passes the conditions:
    n**2+1, n**2+3, n**2+7, n**2+9, n**2+13, and n**2+27
    are each consecutive primes
    '''
    result = True 
    
    return result 

def test_base_case ():
    for x in range( 1,11):
        if check_integer(x):
            print(x, " passes the conditions") # 10 should be the only one that passes
        else:
            print( x, " does not pass teh conditions")