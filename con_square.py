# !/bin/bash/python3
# Daylan Stoica
# @DaylanDStoica


'''
Concealed Square
Problem 206

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
'''

def square_is_valid (number):
    ''' get the square of the number, 
    and return True it fits the form: 1_2_3_4_5_6_7_8_9_0
    return False otherwise
    '''
    
    form = "1_2_3_4_5_6_7_8_9_0"
    sq_number = number**2 # square the given number
    result = True 
    count = 0
    while sq_number > 0:
        # printstr = " before: " , sq_number # for testing the devaluation of the string
        # printstr2 = " before: ", form # comment out all print lines upon completion 
        # print( " first digit of form" , form[-1], count)
        # count += 1
        if sq_number % 10 == int( form[-1] ): # get the last digit of the form 
            pass
            # continue 
        else: 
            result = False 
            # print( " the strings are: ", printstr, printstr2)
            break 
        # shift the string for the next loop
        sq_number = sq_number // 100 # drop the right-most digits, to get the next digit in form 
        
        # form_size = len(form)
        # form = form[:form_size-2] # drop the last 2 chars, _x
        form = form[:-2]
        
        # printstr += " after: ", sq_number
        # printstr2 +=  " after, " , form 
        # print(printstr)
        # print( "   ", printstr2)
    return result


# print ( square_is_valid ( 11221532040)  )

# Note: because of how squares, with the final digit of a being 0
# is likely for the second last digit of the square to also be 0
# 10**2 = 100


def is_last_digit_0( num):
    # return a bool, 
    # if the number ends in 0, return True
    # if the number ends in any other number, return False 
    return ( num%10 == 0)
def proof_2_digits_zero():
    # used to prove that the last 2 digits are zero, when the last digit is itself 0
    count_non_double_zeros = 0
    for x in range ( 1, 10000):
        sq_num = x**2
        if is_last_digit_0( sq_num):
            # if the squares last digit is a 0
            # print( sq_num, " is a square, ending in a 0", " with a base value of: ", x)
            print( " with a base value of: ", x, " , the square that ends in a 0: ", sq_num)
            if ( sq_num % 100 != 0):
                # if the squares last 2 digits is not 0, but last digit is 0
                count_non_double_zeros += 1
                
    print( " the number of squares that end in one zero but not two zeros: ", count_non_double_zeros) # 0
# proof_2_digits_zero()

import math 
def main():
    highest_possible_square = 1929394959697989990 # the highest possible value that any square of a valid form can have 
    lowest_possible_square =  1020304050607080900
    max_square_root = int( math.sqrt(highest_possible_square) ) # the highest the base-number can be, 1389026623
    min_square_root = int( math.sqrt(lowest_possible_square ) ) # the lowest the base_number can be,  1010101010
    
    print( min_square_root) # 1010101010
    for x in range( min_square_root , max_square_root + 1, 10): # check for 1 above the highest possible base-square value 
        # because of the proof that valids can only be of double-zero endings, can increment the loop in 10's
        # pass
        if square_is_valid(x):
            print("found the square-base:           ", x)
            break # upon finding the desired base, exit
        else:
            print( x, " is not the valid square-base")
            
            
main()