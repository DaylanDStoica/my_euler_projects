# Daylan Stoica
# @DaylanDStoica
# 6 December 2022

'''
Licence plates
Problem 371

Oregon licence plates consist of three letters followed by a three digit number (each digit can be from [0..9]).
While driving to work Seth plays the following game:
Whenever the numbers of two licence plates seen on his trip add to 1000 that's a win.

E.g. MIC-012 and HAN-988 is a win and RYU-500 and SET-500 too (as long as he sees them in the same trip).

Find the expected number of plates he needs to see for a win.
Give your answer rounded to 8 decimal places behind the decimal point.

Note: We assume that each licence plate seen is equally likely to have any three digit number on it.
'''

# note: with range of 000-999, then the average would be 499.5 for the number on license plates
# add up to 1000, exactly 


def is_winner ( seen_plates):
    # determine if the list of values presented so far, pass the win condition 
    lower_set = [] # will hold less than 500
    upper_set = [] # will hold more than 500 
    # when the lower and upper are compared, may add up to 1000
    median = [] # only contain values of 500, two 500s add up to win
    for x in seen_plates:
        if x > 500:
            upper_set.append(x)
        elif x < 500:
            lower_set.append(x)
        elif x == 500: 
            median.append(x)
            # if median.len() >= 2: # if there are more than one value of 500, 
            if len(median) >= 2:
                # 500*2 = 1000, winner 
                return True 
            
    # loop through the two sets, if the sum equals 1000, return True 
    # no two values over 501 can add up to 1000
    # no two values less than 499 can add up to 1000
    for l in lower_set:
        for u in upper_set:
            if ( l + u == 1000):
                return True 
            else:
                continue

    return False 



def test_winner_1( seen_plates = [1, 499, 500, 500, 399, 700]):
    '''test the two 500's win condition'''
    if is_winner(seen_plates): # True
        print( seen_plates, " is a winner")

def test_winner_2 ( seen_plates = [ 300, 700, 499]):
    '''test the upper and lower add'''
    if is_winner(seen_plates): # True 
        print( seen_plates, " is a winner")

    
def main():
    seen_plates = [] # list of integers, containing the plates seen on the trip 
    test_winner_1()
    test_winner_2()
    
    
main()