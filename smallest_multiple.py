
# Daylan Stoica
# 10 August 2022

# @DaylanDStoica
# projectEuler  problem #5
'''


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def check_num ( number, top_num = 20):
    result = True
    for x in range(top_num , 1, -1):
        if number % x != 0:
            result = False
            break
    return result

def break_into_prime_list ( number):
    ''' get a list of primes for the number, one entry for each time the prime applies
    use for acquiring the primes of the factors to be considered.
    used for in the get_factor_dict
    return a list of ints'''
    temp_num = number
    primes = 2
    prime_list = []

    return prime_list


def get_factor_list (number):
    # produce the factor list, return for adding to considered factors list
    factor_list = []
    for x in range(1,number+1):
        if number % x == 0:
            factor_list.append(x)
    return factor_list

def get_factor_dict ( number):
    '''count the number of each primes occurence
    use for determining if the prime should be multiplied into the lowest_comm_mult'''
    factor_dict = {}
    factor_list = get_factor_list(number)
    for x in factor_list:
        if not x in factor_dict:
            factor_dict[x] = 1
        else:
            factor_dict[x] += 1

def get_multipled_number( top_number = 20):
    factor_list = []
    prod = 1
    for x in range(top_number, 0 , -1):
        if x in factor_list:
            continue
        else:
            prod *= x
        factor_list += get_factor_list(x)
    return prod , factor_list

def main():
    result = False
    x = 0
    top_number = 20
    add_value , factor_list = get_multipled_number( top_number)
    print("add_value ", add_value)
    while not result:
        # pass
        # break
        x += add_value
        result = check_num(x, top_number)  # passes test of top_num = 10
        print(x)
    print(x)


main()
# correct answer: 232792560
# attempt:     670442572800