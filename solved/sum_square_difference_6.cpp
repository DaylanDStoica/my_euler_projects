
// # Sum square difference
// # Problem 6

// # The sum of the squares of the first ten natural numbers is,
// #     1**2 + 2**2 + ... + 10**2 = 385

// # The square of the sum of the first ten natural numbers is,
// #     ( 1 + 2 + ... + 10)**2 = 55**2 = 3025

// # Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is.
// #     3025 - 385 = 2640

// # Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

// def get_sum_of_squares ( top_value):
//     # 1**2 +2**2 +... + 10**2
//     pass 


#include <iostream>
using namespace std;

int get_sum_of_squares ( int top_value){
    int sum = 0;

    printf(" sum the squares\n\n");
    for ( int x = 0; x <= top_value ; x++){
        printf (" adding %i to %i\n", x*x, sum);
        sum += x*x;  // add the square of the current natural number
    }
    printf("the sum is %i\n\n", sum);
    return sum;
}
// def get_square_of_sum (top_value):
//     # ( 1+2+... +10) **2 
//     sum = 0
    
int get_square_of_sum ( int top_value){
    int sum = 0;

    printf( "sum then square \n\n");
    for ( int x = 0; x <= top_value; x++){
        printf( "adding %i to %i\n", x, sum);
        sum += x;
    }

    int squared_sum = sum*sum;
    printf(" %i is the square of %i\n\n", squared_sum, sum);
    return squared_sum;
}
//     pass

// def get_difference (top_value):
//     # get the difference between the sum-of-squares and the square-of-sums

int get_difference ( int top_value){
    int sum_of_squares = get_sum_of_squares( top_value);
    int square_of_sums = get_square_of_sum( top_value);

    int difference = square_of_sums - sum_of_squares;
    cout << difference << " = " << square_of_sums << " - " << sum_of_squares << endl;
    return difference;
}

int main(){
    // int top_value = 10; // base case

    int top_value = 100;
    int difference = get_difference( top_value);

    cout << difference;
    cout << endl;
    return 0;
}