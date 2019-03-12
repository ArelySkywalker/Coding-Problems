jQuery(document).ready(function($){

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
    * 
    * Author: Arely Miramontes Rodriguez
    * 
    ***************************/

    function findASum(array, sum) {
        for(var i = 0; i < array.length; i++) {
            for(var j = 0; j < array.length; j++) {
                if(array[i] != array[j] && array[i] + array[j] == sum) {
                    return true;
                }else {
                    return false;
                }
            }
        }
    }

    var numbers = [ 10, 15, 3, 7 ];
    var sum = 22;

    console.log(findASum(numbers, sum));

});