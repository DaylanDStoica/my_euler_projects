# Daylan Stoica
# @DaylanDStoica

# 14 December 2022


'''
How many reversible numbers are there below one-billion?
Problem 145

Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. 
For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. 
Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?
'''

def reverse(num):
    ''' 
    inverse the order of digits in the given number, and return the reversed order
    decrease the digits to move forward'''
    rev_num = 0
    while num > 0:
        # removing the right-most digit of num, move it to the right-most digt of rev_num
        rev_num *= 10 # move the rev_num up a digit position
        rev_num += num % 10 # get the right most digit 
        num = num // 10 # remove the right most digit
        
    return rev_num 

def is_valid(num):
    '''if the sum of the number and reversed-number are odd, return True'''
    reversed_sum = num + reverse(num)
    if reversed_sum % 2 == 1 : # if is odd
        return True 
    else:
        return False 
    
    
def main():
    # print ( 1023, reverse(1023) , 1023 + reverse(1023)) # test
    pass
    
main()