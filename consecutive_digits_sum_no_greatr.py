# Daylan Stoica
# @DaylanDStoica
# 15 November 2022

'''
Numbers for which no three consecutive digits have a sum greater than a given value 
Problem 164

How many 20 digit numbers n (without any leading zero) exist such that no three consecutive digits of n have a sum greater than 9?
'''

def check_number_for_digit_count ( number, digit_count = 20):
    pass 


# def sum_digits( number):
from shared_math import sum_digits
    
def find_largest_sum_of_digits ( number):
    '''find the largest sum, from 3 consecutive digits, of a given number
    
    idea: get the last 3 digits, via %1000
    compare to the current largest sum, if bigger than largest_sum, than assign current digit_sum'''
    largest_sum = 0
    while number > 0:
        last_3_digits = number % 1000 #get the 3 right-most digits, and count their sum 
        sum_of_last_3 = sum_digits( last_3_digits)
        if sum_of_last_3 > largest_sum : 
            largest_sum = sum_of_last_3
        number = number // 10  # drop the right-most digit, to progress to loop-end-condition
        
    return largest_sum

def check_for_largest_sum_exceed_number ( number, exceeds_num = 9):
    '''check that if the given number's sum-digits, does not exceed the given exceeds_number
    
    return True if not greater than'''
    if find_largest_sum_of_digits(number) > 9:
        return False 
    else:
        return True 
    
def main():
    starting_number = 10**20 # 20 digit numbers 
    ending_number = 10**21 # 21 digit number, do not go past 
    
    current_number = starting_number 
    count_not_exceeds = 0 # count the number of not exceeding the given number 
    given_exceed_number = 9
    while current_number < ending_number:
        # once the current_number reaches 21-digits, stop 
        if check_for_largest_sum_exceed_number ( current_number, given_exceed_number):
            print( "   ", current_number, " has no 3-consecutive digits that, when summed, do not exceed ", given_exceed_number)
            count_not_exceeds += 1
        else:
            pass 
        current_number += 1
        
        
main()