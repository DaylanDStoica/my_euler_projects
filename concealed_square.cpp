
// Daylan Stoica
// @DaylanDStoica

// 19 September 2022


/*
Concealed Square
Problem 206

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
*/

#include <iostream>
#include <cmath>


using namespace std;


bool check_concealed_square (int square){
    // int squared = math.power(square,2);
    bool result = true;
    float squared = pow(square, 2);

    // string str_squared = itoa(squared);
    string str_squared = to_string(squared);

    string square_form = "1234567890";

    for ( int i = 0, j = 0; i < str_squared.length(); i +=2, j++){
        // go through to have 1_2_3_4_5_6_7_8_9_0 sync with the squared number
        if (str_squared[i] == square_form[j]){
            continue;
        }
        else{
            result = false;
            break;
        }
    }

    return result;
}

int main(){
    return 0;
}