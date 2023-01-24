# Daylan Stoica
# @DaylanDStoica

# 19 August 2022

'''
Coin sums

Project Euler
Problem 31

In the United Kingdom the currency is made up of pound (£) and pence (p). 
There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1*£1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p

How many different ways can £2 be made using any number of coins?
'''

def develop_path():
    '''create a list of values corresponding to the value of coins
    equal to 200p'''
    return []

potential_coins = [ 1, 2, 5, 20, 50, 100] # 2 pounds equals 200 units 

def build_coin_list ( ones, twos, fives, twenties, fifties, hundreds):
    # given a list of integers
    coin_count_list = [ones, twos, fives, twenties, fifties, hundreds]
        # number of each coin, corresponding to the value of each coin. 
        # multiply to get the total value of the coins
    coin_value_sum = 0

    for x in len(potential_coins):
        coin_value_sum += potential_coins[x] * coin_count_list[x]

    return coin_value_sum