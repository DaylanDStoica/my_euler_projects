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
    sq_number = number**2 
    result = True 
    while sq_number > 0:
        if sq_number % 10 == form[-1]: # get the last digit of the form 
            continue 
        else: 
            result = False 
            break 
        # shift the string for the next loop
        sq_number = sq_number // 100 # drop the right-most digits, to get the next digit in form 
        
        form_size = len(form)
        form = form[:form_size-2] # drop the last 2 chars, _x
        
    return result
