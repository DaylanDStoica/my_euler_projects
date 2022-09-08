
//Daylan Stoica
// 6 September 2022

//Project Euler

/*
Powerful digit sum
Problem 56

A googol (10**100) is a massive number: one followed by one-hundred zeros; 
100**100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, 
what is the maximum digital sum?
*/

#include <iostream>
#include <string>

using namespace std;

int sum_digits ( int number)
{
    // get the sum of the digits of the given integer
    // string str_num = string(number);
    int summed_digits = 0;
    while (number > 0)
    {
        // modulus the number by 10, getting the 1's position to add to return
        // then, divide the given number to move the next digit down
        // stop once there are no more digits
        summed_digits += number%10;
        number = number / 10;
        // print(number)
        cout << number << endl;
    }
    return summed_digits;
}

int main(){
    int ret = sum_digits(123456789);
    cout << "sum of digits " << ret;
    return 0;
}