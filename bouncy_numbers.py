
# Daylan Stoica
# @DaylanDStoica
# 19 August 2022

'''Bouncy numbers


Project Euler
Problem 112

Working from left-to-right if no digit is exceeded by the digit to its left
it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right
it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing
a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred,
but just over half of the numbers below one-thousand (525) are bouncy.
In fact, the least number for which the proportion of
bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and
by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%
'''

def is_increasing(number):
    '''each digit is not exceeded by the digit to its left
    [i] <= [i+1], return True'''
    str_num = str(number)
    result = True
    for i in range(1, len(str_num) ):
        # be able to compare the left, to the end
        digit = int(str_num[i])
        digit_left = int(str_num[i-1])
        if digit < digit_left:
            result = False 
            break 
    return result
        
def is_decreasing(number):
    '''each digit is not exceed by the digit to its right
    [i] >= [i+1], return True'''
    str_num = str(number)
    result = True
    for i in range(0, len(str_num) -1):
        # be able to compare to the right, to the end minus 1
        digit = int(str_num[i])
        digit_right = int( str_num[i+1])
        if digit < digit_right:
            result = False 
            break 
    return result
    
def is_bouncy (number):
    '''the rule of each digit being increasing or decreasing is not true
    neither is_increasing nor is_decreasing, both must return False
    account for single value digit-numbers
        ex: 222222
    return boolean'''
    # if is_increasing(number) or is_decreasing(number):
        # return True 
    return not ( is_increasing(number) or is_decreasing(number) )
    # if is increasing == True, return False
    # if is decreasing == True, return False
    # if neither is True, return True

def test_the_is():
    is_count = { 'incr_count' : 0 , 'decr_count' : 0, 'bouncy_count' : 0}
    for x in range(100, 1000):
        if is_increasing(x):
            is_count['incr_count'] += 1
            print(f" {x:5} is increasing")
            continue 
        elif is_decreasing(x):
            is_count['decr_count'] += 1
            print(f" {x:5} is decreasing")
            continue 
        elif is_bouncy(x):
            is_count['bouncy_count'] += 1
            print(f" {x:5} is bouncy")
            continue
        # print(f"\n\n\n{x:10} is none of the above\n\n\n\n")
        
    for k, v in is_count.items():
        print(f"{k:8} : {v}")
        
        
# test_the_is()