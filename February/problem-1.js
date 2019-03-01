jQuery(document).ready(function($){

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
                    }
                }
            }
        }
        if(final != null) {
            console.log(num1 + " + " + num2 + " = " + sum);
        }else {
            console.log("Error: No numbers that could sum to " + sum + " found.");
        }
    }

    var numbers = [ 10, 15, 3, 7 ];
    var sum = 22;

    console.log(findASum(numbers, sum));

});
