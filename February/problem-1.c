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
 * Author: Arely Miramontes Rodriguez
 * 
 ***************************/

#include <stdio.h>

void findASum(int *array, int sum);
void findASum2(int *array, int sum);


int main(int argc, char* argv[]) {

    int numbers[] = { 10, 15, 3, 7 };
    int sum = 22;

    findASum(numbers,sum);
    findASum2(numbers,sum);
}

// Here is my initial solution
void findASum(int *array, int sum){

    printf("My initial solution:\n");

    int num1, num2, check, final;

    for(int i = 0; i < sizeof(*array); i++) {
        int current = array[i];

        for(int j = 0; j < sizeof(*array); j++ ) {
            if(current != array[j]) {
                check = current + array[j];

                if(check == sum) {
                    printf("True");
                }
            }
        }
    }

    printf("\n");
}

// Here is a shorter solution to solve in one pass:
// 
//  Basically the same as my initial, but I used removed
//  uneccessary variables, and made tue if loop better

void findASum2(int *array, int sum) {
    printf("New solution:\n");
    for(int i = 0; i < sizeof(*array); i++) {
        for(int j = 0; j < sizeof(*array); j++) {
            if(i != j && array[i] + array[j] == sum) {
               printf("True");
            }
        }
    }
    printf("\n");
}