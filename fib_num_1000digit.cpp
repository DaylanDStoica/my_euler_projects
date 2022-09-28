
//Daylan Stoica
//@DaylanDStoica

// 15 September 2022 

/*
1000-digit Fibonacci number
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

*/

#include <iostream> 
#include<string>
using namespace std;


int next_fib( int x1, int x2){
    return x1 + x2 ;
}
/*
void fib_sequence ( int* x1, int* x2, int* index){
    int tempX = *x2;
    cout << tempX << " test number pointer" << endl;
    *x2 = next_fib( *x1, *x2);
    *x1 = tempX;
    *index++;

    cout << "index: " << *index << "   " << *x1 << " , " << *x2 << endl;
    
}
*/
void fib_sequence ( double &x1, double &x2, int &index){
    /*
    int tempX = x2;
    cout << tempX << " test number pointer" << endl;
    x2 = next_fib( x1, x2);
    x1 = tempX;
    index++;

    cout << "index: " << index << "   " << x1 << " , " << x2 << endl;
    */
    printf("before function:    index: %d, x1: %f, x2: %f \n", index, x1,x2);

    double& temp = x2;
    x2 = x1 + x2; 
    x1 = temp;
    index++;
    printf("    after function:     index: %d, x1: %f, x2: %f \n", index, x1,x2);
}


int main(){
    double num1 = 1;
    double num2 = 1;
    int index = 1;
    while ( to_string(num2).length() <= 999){
    // while ( num2 < 10**1000){
        // fib_sequence( &num1, &num2, &index);
        fib_sequence(num1, num2, index);
        cout << "number length " << to_string(num2).length();
        // cin.ignore();
    } 
    //loop as long as the number has less than 1000 digits
    return 0;
}