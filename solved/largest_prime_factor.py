# Daylan Stoica
# @DaylanDStoica

#14 August 2022



'''
EulerProject.net

Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from shared_math import build_prime_list
def get_highest_prime_factor(number):
    prime_list = build_prime_list(number)
    highest_prime = prime_list[-1]
    return highest_prime

x = get_highest_prime_factor(600851475143)
print(x)

# solved: 6857
