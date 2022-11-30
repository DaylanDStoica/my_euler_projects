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
    
    return True if not greater than exceeds_num parameter
    return False otherwise'''
    if find_largest_sum_of_digits(number) > exceeds_num:
        return False 
    else:
        return True 

def check_for_largest_sum_exceed_number2 ( number, exceeds_num = 9):
    '''second version of the limit consecutive digits sum code block 
    immediately return False if 3-consecutive digits sum exceed the given number
    
    return False if there exists a 3-digit-sum that exceeds the given number 
    return True if there does not exist such a digit-set
    '''
    result = True # change return result, if any of the digits-sums exceeds the given number
    while number > 0:
        last_3_digits = number % 1000 
        sum_of_last_3 = sum_digits(last_3_digits) 
        if sum_of_last_3 > exceeds_num:
            result = False 
            break 
        else:
            pass
        number = number // 10
    return result 

    
# def main():
def loop_and_count_digitsets():
    starting_number = 10**20 # 20 digit numbers 
    ending_number = 10**21 # 21 digit number, do not go past 
    
    current_number = starting_number 
    count_not_exceeds = 0 # count the number of not exceeding the given number 
    given_exceed_number = 9 # the given number that sums cannot exceed
    while current_number < ending_number:
        # once the current_number reaches 21-digits, stop 
        # if check_for_largest_sum_exceed_number ( current_number, given_exceed_number):
        if check_for_largest_sum_exceed_number2 ( current_number, given_exceed_number):
            print( "   ", current_number, " has no 3-consecutive digits that, when summed, do not exceed ", given_exceed_number)
            count_not_exceeds += 1
            print("current count: ", count_not_exceeds)
        else:
            pass 
        current_number += 1
        
        
# main()

    
def find_largest_set_of_digits ( number, exceeds_num = 9, digit_count = 20):
    ''' find the set of digits that exceed the number, and immediately increment that number
    1000001450033, take 100000145 to 100000146, then bring back to 20 digits. => 1000001460000
    return that higher number
    
    reason: if an unacceptable digit-set is in the millions, then millions of increment operations
    on the original test-number will be performed, before being able to find the next available
    purpose: speed up the that operations loop, by clearing the number of leading numbers before the digit-set
    incrementing the resulting base, and filling back up the leading zeros
    '''
    min_number = 10**digit_count # the number that the returned number must be greater than 
    if check_for_largest_sum_exceed_number2 ( number, exceeds_num):
        # the number has a digit-set that exceeds the number 
        # reduce, find the highest set of 3-digits, then return the fixed number 
        # while number > 0:
        #     last_3_digits = number % 1000 
        #     sum_of_last_3 = sum_digits(last_3_digits) 
        #     if sum_of_last_3 > exceeds_num:
        #         result = False 
        #         break 
        #     else:
        #         pass
        #     number = number // 10
        while number > 0:
            # loop degrading the number, until you get to the lowest set of number-exceeding digits
            last_3_digits = number % 1000 
            if sum_digits(last_3_digits) > exceeds_num:
                break
            number = number // 10
        # number += 1 # increasing the lowest number of the digits by one
        while number < min_number:
            # loop increasing the number, until it has 20 digits again
            number *= 10
        number += 1 # increasing the lowest number of the digits by one

    else:
        # return number
        # do nothing to the number if there are no invalid digit-sets for counting, 
        # simply return the original number
        pass 
    return number 

def loop_and_count_digitsets2( lower_digits = 20, upper_digits = 21, exceeds_num = 9):
    '''same as before, but with the find_largest_set_of_digits implented for faster counting'''
    starting_number = 10**lower_digits # start at 20-digit numbers 
    ending_number = 10**upper_digits # end at 21-digit numbers
    
    current_number = starting_number
    count_digitsets = 0 # counter variable
    while current_number < ending_number:
        # as long as the current_number has less than 21-digits
        pass 
        # TODO: develop way to check if the number, after skipping over the invalid upper digit-sets, 
        # to check if the new number is not also invalid
        print( "current_number, before digit skip: ", current_number)
        current_number = find_largest_set_of_digits( current_number, exceeds_num)
        print( " current number, after digit skip: ", current_number)
        
        # conditionally incremnt the counter
        if check_for_largest_sum_exceed_number2( current_number, exceeds_num):
            print( "current number is valid, incrementing counter: ")
            count_digitsets += 1
            print("     count_digitsets = ", count_digitsets)
        current_number += 1 #increment the current number, after skipping the invalid chunks
    return count_digitsets

def main():
    print("beginning the loopfunction")
    digitsets_count = loop_and_count_digitsets2()
    completion_message = " the total number of 20-digit positive integers, with sums of 3 consecutive digits is: "
    print( completion_message, digitsets_count)
    
    
main()