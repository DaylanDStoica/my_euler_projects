#!/usr/bin/env python3

# Daylan Stoica
# 
# @DaylanDStoica
# 10 August 2022

# Problem #48 on ProjectEuler.net

'''


The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

'''


def self_power ( number):
    return number**number

def loop_power_sum ( top_lim = 1000):
    sum = 0
    for x in range(1, top_lim + 1):
        sum += self_power(x)
        print(f" x{x},  self_power{self_power(x):8},  sum{sum:12}")

    return sum

def main():
    sum = loop_power_sum()
    print("sum ", sum)

    str_sum = str(sum)
    len_str = len(str_sum)
    # print("last 10 digits ", str(sum)[:len(str(sum)-10)])
    print("last 10 digits ", str_sum[len_str-10:])

main()