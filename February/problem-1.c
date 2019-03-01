/****************************
 *
 * PROBLEM 1:  
 *              Given a list of numbers a number k
 *              return whether any two numbers from the
 *              list add up
 *
 *              given [10, 15, 3, 7]
 *              and k of 17
 *              return true since 10 + 7 = 17
 * 
 ***************************/

#include <stdio.h>

void findASum(int *array, int sum);


int main(int argc, char* argv[]) {

    int numbers[] = { 10, 15, 3, 7 };
    int sum = 22;

    findASum(numbers,sum);
}

void findASum(int *array, int sum){

    int num1, num2, check, final;

    for(int i = 0; i < sizeof(*array); i++) {
        int current = array[i];

        for(int j = 0; j < sizeof(*array); j++ ) {

            if(current != array[j]) {
                check = current + array[j];

                if(check == sum) {
                    num1 = current;
                    num2 = array[j];
                    final = sum;
                }
            }
        }
    }
    
    if(final == sum) {
        printf("%d + %d = %d", num1, num2, sum);
    }else {
        printf("Error: No numbers that could sum to %d found.", sum);
    }
}