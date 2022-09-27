/*
Daylan Stoica
@DaylanDStoica
27 September 2022

Mission statement: 
    practice parsing strings, for this case parse a math expression into components
    to be computed
*/


#include <iostream>
// #include <string>
using namespace std;

class int_parse{ public:
    //operation that separates left from right

    int left_op;
    char operation;
    int right_op;
};

char* convert_string_to_chararr ( string expression){
    //parse the mathematical equation into separate equations
    //return an array of chars to then be processed 
    int exp_length = expression.length();
    char exp_arr[exp_length];
    for ( int i = 0; i < exp_length; i++){
        exp_arr[i] = expression[i];
    }
    return exp_arr;
}

void parse_chararr ( char* exp_arr){
    // parse the char_array from convert_string_to_chararr function
    char operations[6] = { '+', '-', '*', '/', '%', '='};
    char decimal = '.';
}

int main(){
    return 0;
}