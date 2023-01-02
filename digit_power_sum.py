# Daylan Stoica
# @DaylanDStoica

# 1 January 2023

'''
Digit power sum
Problem 119
The number 512 is interesting because it is equal to the sum of its digits 
raised to some power: 5 + 1 + 2 = 8, and 8**3 = 512. Another example of a number 
with this property is 614656 = 28**4.

We shall define an to be the nth term of this sequence and insist that a 
number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
'''

from distutils.command import check


def separate_the_digits ( number):
    '''separate the digits of number <integer> into an array, and return the array'''
    # int_num = int(num)
    int_num = number 
    digits_array = []
    while  int_num > 0:
        digits_array.insert(0, int_num%10)
        int_num = int_num // 10
    # print(digits_array)
    return digits_array

def tests():
    test1()

def test1():
    for x in range( 1000):
        print(x, "   ", separate_the_digits(x))

# tests()

def sum_the_digits( number):
    '''take the digits from the integer, and return the sum of the digits'''
    digit_array = separate_the_digits(number)
    sum = 0
    for x in digit_array:
        sum += x
    return sum

def check_digitsum_power ( number):
    ''' check if the sum of digits from number, when given any exponent, 
    returns the starting number

    number == digit_sum(number)**(power)
    '''
    result = False
    digit_sum = sum_the_digits(number)
    for power in range(1, 10):
        if number == digit_sum**power:
            result = True 
            print( number, "passes the digitsum_power")
            break 
        # found the next value goal
        else:
            continue

    # return result, number, digit_sum, power
    return result 


# def check_digitsum_power ( number):

def main():
    num = 1
    count = 0
    # for count in range(0,30):
        # count the number of passing values that have been found 
        # while not check_digitsum_power(x):
    passing_array = [] # the array contiaining the numbers that pass
    while count < 30:
        # count the number of passing values that have been found
        if check_digitsum_power(num):
            count += 1
            passing_array.append(num)
            print(num, " added to the array")
            print(passing_array)
        num += 1

    print(num)
    return num , passing_array


# main()

def base_case_test():
    '''You are given that a2 = 512 and a10 = 614656.'''
    count_valids = 0 
    x = 10
    print("base case test: a2 = 512, a10 = 614656")
    while count_valids < 10: # go up to a10
        if check_digitsum_power(x): # if x is a valid number 
            count_valids += 1
            print( "a", count_valids, " = ", x)
        x += 1
        
base_case_test()