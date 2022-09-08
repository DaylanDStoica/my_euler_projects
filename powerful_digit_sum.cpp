
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
        // cout << number << endl;
    }
    return summed_digits;
}

int power( int a , int b){
    // return the value of the input a to the power of input b
    if ( a == 1 || b == 0){
        //immediately return 1 if the 1**b or a**0
        return 1;
    }
    int result = 1;
    for ( int i = 0; i < b ; i++){
        result *= a;
    }
    return result;
}

int power_sum ( int a , int b){
    //return the sum of the digits of the result of the exponent a**b
    int power_val = power(a, b);
    int sum = sum_digits(power_val);
    return sum;
}
int main(){
    //int ret = sum_digits(123456789);
    //cout << "sum of digits " << ret;

    for ( int i = 0 ; i < 14 ; i++){
        for (int j = 0; j < 20; j++){
            cout << i << "**" << j << " = " << power(i,j);
            cout << "  sum_digits: " << power_sum(i,j) << endl;
        }
    }
    return 0;
}