
# Daylan Stoica
# 8 August 2022

# @DaylanDStoica

# Probelm #1 on ProjectEuler.net
"""


If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def is_mult_of_3_or_5( number):
    '''check if the given number is a multiple of 3 or 5
    return True if divisible by 3 or 5, return False otherwise'''
    return (number % 3 == 0) or (number % 5 == 0) 

def get_the_sum_of_mults( up_to_num = 1000):
    sum = 0
    print("sum: ", sum)
    for x in range( up_to_num ):
        if is_mult_of_3_or_5(x):
            sum += x
            print(f"x : {x}  ,    sum : {sum}")

    print(f"final sum of numbers below {up_to_num}:  {sum}")
    return sum


def main():
    sum = get_the_sum_of_mults()

if __name__ == '__main__':
    main()