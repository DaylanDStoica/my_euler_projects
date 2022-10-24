
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

int power_sum_digits ( int a , int b){
    //return the sum of the digits of the result of the exponent a**b
    int power_val = power(a, b);
    int sum = sum_digits(power_val);
    return sum;
}

int find_highest_powerDigitSum ( int highest_base = 100, int highest_exp = 100){
    int highest_digit_sum = 1;
    for ( int a = 1 ; a < highest_base ; a++){
        for ( int b = 1 ; b < highest_exp ; b++){
            int curr_sum_digits = power_sum_digits(a,b);
            if ( curr_sum_digits > highest_digit_sum){
                highest_digit_sum = curr_sum_digits;
                cout << "new highest digit_sum: " << highest_digit_sum;
                cout << " = " << a << "**" << b ;
                cout << " power = " << power(a,b);
                cout << endl;
            }
        }
    }
    return highest_digit_sum;
}
int main(){
    //int ret = sum_digits(123456789);
    //cout << "sum of digits " << ret;

    /*
    for ( int i = 0 ; i < 14 ; i++){
        for (int j = 0; j < 20; j++){
            cout << i << "**" << j << " = " << power(i,j);
            cout << "  sum_digits: " << power_sum_digits(i,j) << endl;
        }
    }
    */
    
    int a = 100, b = 100;
    int max_power_digit_sum = find_highest_powerDigitSum(a,b);
    cout << " highest digit sum from powers " << a << " and " << b ;
    cout << endl << "   " << max_power_digit_sum << endl;
    // result = 74, incorrect
    return 0;
}