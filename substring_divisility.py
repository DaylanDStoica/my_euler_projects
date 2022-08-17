# Daylan Stoica
# @DaylanDStoica

# 15 August 2022

'''
Project Eueler
Sub-string divisibility
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

# each substring of 3 consecutive digits is divisible by an increasing prime

# pandigital : 10 digit number, with each digit being of 0-9
    # 1234567890

digit_nums = '0 1 2 3 4 5 6 7 8 9'.split()
# print(digit_nums)
def is_pandigital( number):
    '''check that the number is pandigital
    length 10, has all of 0-9
    return boolean'''
    number = int(number)
    str_num = str(number)
    # if number >= 10**8 and len(str_num) == 10 and number <= 10**10:
    #     # 0123456789 - 9876543210
    #     print("10**")
    # else:
    #     return False
    if number < 10**8 or number > 10**10:
        # number either has too low or too high value to be possible
        return False

    if len(str_num) == 9:
        # because 0 is not persisted in leading number for int
        # restore the 0 in string form at the front
        str_num = '0' + str_num

    # digit_list = digit_nums
    held_digits = []
    for c in str_num:
        # go through the digits of the number
        # checking off the numbers as they are encountered, pop
        # if not c in digit_list:
        #     # c digit was already encountered, cannot do twice
        #     return False
        # else:
        #     digit_list.remove(c) 
        if c in held_digits:
            # digit c is already encountered
            return False
        else:
            held_digits.append(c)
            

    return True

def test_is_pandigital():
        
    # is_pandigital(1234567890)
    x = 1234567809
    for y in range(x, x+90):
        print(f"{y} is pandigital: {is_pandigital(y)}")

    x = [1234567890, 987654321, 3526174890]
    for y in x:
        print(f"{y} is pandigital: {is_pandigital(y)}")


def build_list_of_substrings(number):
    '''build the list of substrings, each of length 3, moving forward 1 index'''
    # assumes length of at 5
    # starting from second index, to +3 resulting in last index
    substring_list = []
    str_num = str(number)
    for i in range(1, len(str_num) - 2):
        substr = str_num[i: i+3]
        substring_list.append(substr)
    return substring_list

# substr_list = build_list_of_substrings(1234567890)
#     # '234 345 456 567 678 789 890'.split()
# print(substr_list)


# 1. build to check that number is pandigital
# 2. once the pandigital is confirmed, build the substrings
# 3. with the substring list of each pandigital, check for fitting the property
    # property: the substring is divisible by increasing prime
    # s1%2, s2%3, s3%5, s4%7

from shared_math import is_prime

def check_pandigital_substrs(number):
    '''check the subtrings for adequate divisibility property
    return True if passes the property'''    
    substr_list = build_list_of_substrings(number)
    curr_prime = 2 # the current prime for checking the divisibilty
        # 2, 3, 5, 7, 11, 13, 17
    result = True
    for s in substr_list:
        x = int(s)
        while not is_prime(curr_prime):
            curr_prime += 1
        print("current prime: ", curr_prime)
        print(f"{x} % {curr_prime} = {x%curr_prime}")
        if x%curr_prime == 0:
            # passes the divisibility property for the current substring
            curr_prime += 1 
                # move onto the next prime for the next operation
            continue
        else:
            result = False
            break
    return result

def test_check_pan_substrs():
    '''test that the check_pan_substrs function works'''
    num_list = [1234567890, 1406357289]
    for x in num_list:
        print( check_pandigital_substrs(x), x)

# test_check_pan_substrs()