#!/usr/bin/env python3

# Daylan Stoica
# 
# @DaylanDStoica
# 9 August 2022

# Problem #104 on ProjectEuler.net

'''


The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
'''

def check_numbers_back (number):
    '''check the last 9 digits for containning numbers 1-9'''

    # get the last 9 digits of the number
    back_str = str(number)
    back_str = back_str[len(back_str)-9:]
    # print(back_str)

    result = check_that_all_nums_in_str(back_str)

    return result

def check_numbers_front (number):
    '''check the first 9 digits for containing numbers 1-9'''

    # get the first 9 digits of the number
    front_str = str(number)[:9]
    # print(front_str)

    result = check_that_all_nums_in_str(front_str)

    return result

# check_numbers_front(123456789)
numbers_search = '123456789'

def check_that_all_nums_in_str ( number):
    num_str = str(number)
    result = True
    for x in numbers_search:
        if not x in num_str:
            result = False
            break
    return result

# print( check_that_all_nums_in_str(234516789))


def check_numbers_ends (number):
    # return check_numbers_front and check_numbers_back
    front = check_numbers_front(number)
    back = check_numbers_back(number)
    return front and back

print(check_numbers_ends( 1234567890987654321) )


def fibonnaci_sequence ( a, b):
    c = a + b
    # a = b
    return b, c

import keyboard
import time
def key_press_print_check():
    if keyboard.is_pressed('e'):
        return True
    return False

def main():
    a = 1
    b = 1
    print(a,b)
    count = 1
    # for _ in range(10):
    #     a,b = fibonnaci_sequence(a,b)
    #     print(a,b)
    result = False
    while not result:
        a,b = fibonnaci_sequence(a,b)
        count += 1
        # if key_press_print_check():
        # if keyboard.is_pressed('e'):
            # print(b, count)
        result = check_numbers_ends(b)
        # result = check_numbers_front(b)r

        if check_numbers_back(b) or check_numbers_front(b):
            print(b)
            # time.sleep(1)


    print( f"b={b}    ,  short_b={str(b)[:9]}   count={count}")
if __name__ == '__main__':
    main()