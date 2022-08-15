
# Daylan Stoica
# @DaylanDStoica

# 14 August 2022

'''
Digit power sum
Problem 119, EulerProject.net

The number 512 is interesting because it is equal to the sum of its 
    digits raised to some power: 5 + 1 + 2 = 8, and 8**3 = 512.
Another example of a number with this property is 614656 = 28**4.

We shall define an to be the nth term of this sequence and
insist that a number must contain at least two digits to have a sum.
    # number >= 10
You are given that a2 = 512 and a10 = 614656.

Find a30.
'''

"""
notes on values in the sequence:
a1 = 81 = 9**2
a2 = 512 = 8**3

a10 = 614656 = 28**4
"""

def sum_the_digits (number):
    '''sum the digits of the number'''
    sum = 0
    str_num = str(number)
    for x in str_num:
        if x == '.':
            continue
        sum += int(x)
    return sum

def check_powers_sum(number):
    number = int(number)
    digit_sum = sum_the_digits(number)
    for x in range(100):
        if number == digit_sum ** x:
            # print(f"digit_sum {digit_sum:8} from number {number:12}, with power {x:4}")
            return digit_sum, x

    return digit_sum , None
def build_the_sequence( n = 30):
    power = None
    number = 10
    a = 1
    dps_sequence = {}
    while a <= n:
        number += 1
        # print(number)
        digit_sum , power = check_powers_sum(number)
        # print("   ", digit_sum, power)
        if power != None:
            dps_sequence[a] = {digit_sum, power}
            # dps_sequence[a] = 0
            print(f"sequence count a{a:3}, digit_sum {digit_sum:8} with power {power:4} \
            {number}")
            # reset power for 
            power = None
            a += 1 #inctement the sequence count


build_the_sequence()