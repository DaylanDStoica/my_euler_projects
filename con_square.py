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