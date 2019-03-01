var num1 = 1;
var num2 = 100;

function fizzBuzz(min, max) {
    for(i = min; i <= max; i++) {
        if(i % 3 == 0 && i % 5 == 0) { 
            console.log("FizzBuzz"); 
        }else if(i % 3 == 0) {
            console.log("Fizz");
        }else if(i % 5 == 0) {
            console.log("Buzz");
        }else { console.log(i); }
    }
}

fizzBuzz(num1,num2);