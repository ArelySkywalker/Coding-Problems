/****************************
 *
 * PROBLEM 2:  
 *              Given an array of integers, return a new array 
 *              such that each element at index i of the new 
 *              array is the product of all the numbers in the 
 *              original array except the one at i.
 *
 *              input:  [1, 2, 3, 4, 5]
 *              output: [120, 60, 40, 30, 24]
 *
 *              input:  [3, 2, 1]
 *              output: [2, 3, 6]
 * 
 * Author: Arely Miramontes Rodriguez
 * 
 ***************************/

function productOfArrayExceptSelf(array){
    var resultArray = [], product;
    for(var i = 0; i < array.length; i++){
      product = 1;
      for(var j = 0; j < array.length; j++){
         if(i !== j) product *= array[j];
      }
      resultArray.push(product);
    }
    return resultArray;
}

// Sample data
var array   = [1, 2, 3, 4, 5];
var array2  = [3, 2, 1];

console.log(productOfArrayExceptSelf(array));
console.log(productOfArrayExceptSelf(array2));