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
    result = True 
    if len(str_num) % 2 ==1 : # length is odd
        for i in range ( ceil( len(str_num)/2) - 1):
            if str_num[i] == str_num[-1-i]:
                # return True
                continue
            else:
                result = False
                break
    else:
        for i in range( ceil(len(str_num)/2) ):
            if str_num[i] == str_num[-1-i]:
                # return True
                continue
            else:
                result = False
                break
    # return False
    return result

def test_is_palindrome():
    for x in range(3, 100000):
        if is_palindrome(x):
            
            print(f" {x} is palindrome: {is_palindrome(x)}")
        
# test_is_palindrome()

def loop_through_3x3():
    '''go through the loops for the product of all products from 2 3-digits numbers'''
    highest_palindrome = 100*100
    for a in range(100,1000): # 100-999
        for b in range(a,1000): # with a, no repeating lower numbers
            prod = a*b
            if is_palindrome(prod): # if the product is a palindrome
                if prod > highest_palindrome: # update the highest palindrome
                    highest_palindrome = prod
                    print(f" {a}*{b} = {prod}, is a palindrome")
            # else: # not a palindrome product
                # continue
    print("highest palindrome ", highest_palindrome)
                    
                    
                    
loop_through_3x3()