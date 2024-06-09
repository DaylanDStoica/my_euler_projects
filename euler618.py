# <p>Consider the numbers $15$, $16$ and $18$:<br>
# $15=3\times 5$ and $3+5=8$.<br>
# $16 = 2\times 2\times 2\times 2$ and $2+2+2+2=8$.<br>
# $18 = 2\times 3\times 3$ and $2+3+3=8$.<br> 

# $15$, $16$ and $18$ are the only numbers that have $8$ as sum of the prime factors (counted with multiplicity).</p>
# <p>
# We define $S(k)$ to be the sum of all numbers $n$ where the sum of the prime factors (with multiplicity)  of $n$ is $k$.<br>
# Hence $S(8) = 15+16+18 = 49$.<br>
# Other examples: $S(1) = 0$, $S(2) = 2$, $S(3) = 3$, $S(5) = 5 + 6 = 11$.</p>
# <p>
# The Fibonacci sequence is $F_1 = 1$, $F_2 = 1$, $F_3 = 2$, $F_4 = 3$, $F_5 = 5$, ....<br>
# Find the last nine digits of $\displaystyle\sum_{k=2}^{24}S(F_k)$.</p>


from shared_math import build_prime_list
# build_prime_list will return the list of prime numbers , including repeats, to get the given positive integer, not including 1


def get_prime_list_sum ( number) : 
    # given a poistive integer, use the build_prime_list function to get the list of primes, 
    # and return the summation of the contents of the list
    prime_list = build_prime_list( number) 
    sum = 0
    for x in prime_list:
        sum += x 

    return sum

# x = 18
# print( x , " prime list: ", build_prime_list(x), ". Sum of primes: ", get_prime_list_sum(x))