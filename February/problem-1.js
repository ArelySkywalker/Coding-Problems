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
    ***************************/

    function findASum(array, sum) {
        var num1, num2, check, final;

        for(var i = 0; i < array.length; i++) {
            var current = array[i];

            for(var j = 0; j < array.length; j++) {
                if(current != array[j]) {
                    check = current + array[j];

                    if(check == sum) {
                        num1 = current;
                        num2 = array[j];
                        final = sum;
                        return true;
                    }
                }
            }
        }
    }

    var numbers = [ 10, 15, 3, 7 ];
    var sum = 22;

    console.log(findASum(numbers, sum));

});
