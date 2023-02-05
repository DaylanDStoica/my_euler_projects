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

How many reversible numbers are there below one-billion (10**9)?
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
    '''if the sum of the number and reversed-number, has digits that are all odd, return True
    leading zeroes in either direction are unacceptable/unconsidered'''
    
    # check for leading zeroes, that exist when reversed 
    if num % 10 == 0: # right-most digit is 0, that is a leading zero when flipped 
        return False
    
    # check that the sum of [ num + reverse(num)] is odd
    reversed_sum = num + reverse(num)
    # print( num, reverse(num))
    # print(" reversed sum ", reversed_sum)
    # if reversed_sum % 2 == 1 : # if the sum is odd
        # return True 
    # else:
        # return False 
    
    # break up the digits of the sum into a list, for checking for non-odds
    sum_digits = [] 
    while reversed_sum > 0: 
        sum_digits.append( reversed_sum%10) # add the right-most digit to the list 
        reversed_sum = reversed_sum // 10  # drop the right-most digit 

    # print( "list of sums: " , sum_digits)

    result = True 
    # go through the list of reversed sum_digits, checking for non-odds.
    # immediately return False if even is encountered 
    for x in sum_digits:
        if x % 2 == 0: # the digit in the list is even, return False 
            result = False 
            break 
# is_valid( 12237) # check the is_valid function successfully flips, sums, and booleans the given number
def base_case_test():
    '''there are 120 reversible numbers before one-thousand
    check that 120 is returned'''
    count = 0
    for x in range(1, 1000): #less than one-thousand
        if is_valid(x):
            count += 1
            
    print( " count of reversible numbers is: ", count)
    print("         count should be 120")
    
# base_case_test()


def main():
    # print ( 1023, reverse(1023) , 1023 + reverse(1023)) # test
    count = 0
    for x in range(1, 10**9): #from 1 to 1 billion
        # sum_reversed = x + reverse(x)
        if is_valid(x):
            count += 1
    return count
# main()

