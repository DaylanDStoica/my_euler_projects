# Daylan Stoica
# @DaylanDStoica

# 21 August 2022

'''
Largest palindrome product


Project Eueler
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers 
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
from math import ceil
def is_palindrome(num):
    '''boolean, check that the num/string is a palindrome, same back-to-front'''
    str_num = str(num)
    if len(str_num) == 1: #single char 
        return True 
    # for i in range( len(str_num) ):
    for i in range ( ceil( len(str_num)/2) - 1):
        if str_num[i] == str_num[-1-i]:
            return True 
    return False

def test_is_palindrome():
    for x in range(3, 500):
        print(f" {x} is palindrome: {is_palindrome(x)}")
        
# test_is_palindrome()