#!/usr/bin/env python3

# Daylan Stoica
# 
# @DaylanDStoica
# 10 August 2022

# Problem #16 on ProjectEuler.net


'''


2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

def sum_the_digits(number):
    '''sum the digits of the number'''
    str_num = str(number)
    sum = 0
    for x in str_num:
        sum += int(x)
    return sum

def main():
    num = 2**15
    print(f"number {num}, sum {sum_the_digits(num)}")

    num = 2**1000
    print(f"number {num}, sum {sum_the_digits(num)}")

main()