
# Daylan Stoica  
# @DaylanDStoica

# 18 October 2022
'''
Double-base palindromes
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

from tabnanny import check


def is_palindrome( number):
    '''read a string, and return true if palindrome
    palindrome: same order of chars when being read forward or back'''
    result = True 
    str_num = str(number)
    # i = 0
    # for ( i < len(str_num) ):
    for  i in range ( len(str_num) //2 ) :
        if str_num[i] == str_num[-(i+1)]:
            # check the values at the index, and at the other side of the index
            continue
        else:
            result = False 
            break

    return result 

def check_both_palindromes( number):
    '''convert a number into two strings,
    one for integer, one for binary.
    and check the palindrome status of both strings.
    return True if both strings are palindromes'''
    # int_num = format(number, 'i')
    int_num = number
    binary_num = format(number, 'b')
    # print(int_num, binary_num)
    if is_palindrome(int_num) and is_palindrome(binary_num):
        print("are both palindromes")
    return is_palindrome(int_num) and is_palindrome(binary_num)


# check_both_palindromes( 25)
def test_check_palindromes():
    for i in range(1, 10000):
        if is_palindrome(i):
            # if the integer is a palindrome
            # print( i , "is a palindrome")
            pass
        if check_both_palindromes(i):
            # if both integer and binary are palindrome (the goal)
            print( i , format(i, 'b') , "are both palindromes")
        else:
            # in case the integer is palindrome, but the binary is not
            # print( format(i, 'b') , "is however not a palindrome")
            pass
        


# test_check_palindromes()


def base_case():
    '''
    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
    '''
    sum = 0
    for x in range(1, 1000000):
        if check_both_palindromes(x):
            print( '    ', x, format(x,'b'))
            sum += x 

    print( "sum of palindromes: ", sum)
    return sum

base_case()