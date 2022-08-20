
# Daylan Stoica 
# @DaylanDStoica

# 19 August 2022

'''
Permuted multiples


Project Eueler
Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def check_for_same_digits (num1, num2):
    '''return boolean,
    check if the two numbers shared the same digits, 
    albeit in different order'''
    str_num1 = str(num1)
    str_num2 = str(num2)
    if len(str_num1) != len(str_num2):
        # if two numbers do not have the same number of digits, return False
        return False
    for c in str_num1:
        if c not in str_num2:
            # a digit in num1 does not exist in num2
            return False
    for c in str_num2:
        if c not in str_num1:
            # a digit in num2 does not exist in num1
            return False
    # passing the requirements, return True
        #same length, and possessing the same digits in both directions
    return True

def check_the_multiples (number, multiples = 6):
    '''check the multiples of the number for same digits'''
    for x in range(1,multiples+1):
        if not check_for_same_digits(number, number*x):
            #the digits are not shared with the multiple
            
            return False
        else:
            print(f"{number} and {number*x} have the same digits")
    return True

def main():
    x = 1
    while True:
        if check_the_multiples(x):
            break
        else:
            x += 1
        
    #once the lowest positive integer is found
    print(x, " has same digits for its multiples")
    print( x, x*2, x*3, x*4, x*5, x*6)
    
main()