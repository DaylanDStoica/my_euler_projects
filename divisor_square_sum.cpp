
/*
Daylan Stoica
@DaylanDStoica

*/

/*
Divisor Square Sum
Problem 211

For a positive integer n, let σ2(n) be the sum of the squares of its divisors. For example,
σ2(10) = 1 + 4 + 25 + 100 = 130.

Find the sum of all n, 0 < n < 64,000,000 such that σ2(n) is a perfect square.
*/

#include <iostream>
using namespace std;



int* find_divisors( int num){
    // return an array of integers of the num's divisors
    int* divisor_list;
    int x = 1;
    if ( num <= 0){
        return divisor_list;
        // return an empty array if the num is zero or negative
    }
    for (int i = 0; x < num; i++, x++){
        if ( num % x == 0){
            // an even division is added to the list
            divisor_list[i] = x;
            cout << x << " added to divisor list";
        }
    }
    cout << endl;
    return divisor_list;

}

int main(){
    for ( int x = 1; x < 20; x++){
        int* div_arr = find_divisors(x);
        int* div_arr_ptr = div_arr;
        // generate the list of divisors for the number in the loop, then print them out for testing

        // int i = 0;
        cout << "starting number: " << x;
        cout << endl;
        cout << "   divisor list: ";
        // while (div_arr[i] != nullptr){
            // cout<< ", %d" << div_arr[i];
            // i++;
        // }
        while ( div_arr_ptr != NULL){
            cout << ", " << *div_arr_ptr;
            div_arr_ptr++;
        }
        cout << endl;
    }

    return 0;
}