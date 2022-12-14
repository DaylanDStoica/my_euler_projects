
# Daylan Stoica
# 
# @DaylanDStoica
# 8 August 2022

# Problem #2 on ProjectEuler.net

'''


Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def get_next_fib_num( a , b):
    return a+b

def get_next_chain_fib ( a,b):
    return b, a+b 

def is_even (number):
    return (number%2 == 0)

# def main( no_higher_than = 4* 1000000):
def main( no_higher_than = 4000000):
    # no higher than a value of 4 million

    # start the fibonnaci sequence
    a = 1
    b = 1

    sum = 0
    sum_list = []
    fib_list= [ a, b]
    while b <= no_higher_than:
        print(a,b)
        print( f"  {a} + {b} = {a+b}")
        fib_list.append(b)
        if is_even(b):
            print("even b: ", b)
            # print(b)
            sum += b
            print("sum: ",sum)
            sum_list.append(b)
        a,b = get_next_chain_fib(a,b)
        # fib_list.append(b)

    print("sum:  ", sum)
    print("even_list: ", sum_list)
    print("whole fib list: ", fib_list)

if __name__ == '__main__':
    main()