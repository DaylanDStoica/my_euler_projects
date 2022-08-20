# Daylan Stoica
# @DaylanDStoica

# 19 August 2022

'''
Digit factorials


Project Eueler
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

def factorial(number):
    prod = 1
    if number == 1 or number == 0:
        return 1
    elif number == 2:
        return 2
    for x in range( number, 1, -1):
        print("Factorial x is ", x)
        prod *= x
        print("    prod = ", prod)
    return prod

# def factorial(number):
#     if number == 1:
#         return 1
#     return number*factorial(number-1)

def break_num_into_digits(number):
    '''return the list of digits of the number'''
    # str_num = str(number)
    # listdigit_list = {for x in }
    # num = 13579
    x = [int(a) for a in str(number)]
    # print(x)
    return x

def get_sum_of_factorial_digits(number):
    '''get the sum of digit's factorials'''
    # factorial = factorial(number)
    digit_list = break_num_into_digits(number)
    fact_sum = 0
    for x in digit_list:
        fact_x = factorial( int(x) )
        fact_sum += fact_x
    return fact_sum

def check_factorial_digits(number):
    '''check that the sum of each digit's factorial equal the original number'''
    fact_sum = get_sum_of_factorial_digits(number)
    return number == fact_sum
    
    
import time 
def sum_the_passed_nums(upper_range = 10000):
    '''Find the sum of all numbers which are equal to the 
    sum of the factorial of their digits.'''
    # x = 3 
    # while True:
    sum = 0
    for x in range(3, upper_range):
        print(x)
        time.sleep(0.1)
        if check_factorial_digits(x):
            sum += x
            print("\n\n\n ", sum, "\n\n\n\n")
            time.sleep(1)
    return sum
def main():
    # for x in range(1,100):
    #     # print("factorial of ", x , " = ", factorial(x) )
    #     print(" factorial of digits of ", x, " = ", get_sum_of_factorial_digits(x))
    
    # x = 3
    # while True:
    #     if check_factorial_digits(x):
    #         break
    #     x += 1
    # print(" the factorial of digits of ", x, " = ", get_sum_of_factorial_digits(x))

    print("sum of the passed numbers: ", sum_the_passed_nums() )
        
main()