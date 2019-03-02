##############################
 #
 # PROBLEM 2:  
 #              Given an array of integers, return a new array 
 #              such that each element at index i of the new 
 #              array is the product of all the numbers in the 
 #              original array except the one at i.
 #
 #              input:  [1, 2, 3, 4, 5]oh no 
 #              output: [120, 60, 40, 30, 24]
 #
 #              input:  [3, 2, 1]
 #              output: [2, 3, 6]
 #
 # Author: Arely Miramontes Rodriguez
 # 
##############################

def indexProductExcepti(array):
    resultArray = []
    for i in range(len(array)):
        product = 1
        for j in range(len(array)):
            if i != j: product *= array[j]
        resultArray.append(product)
    return resultArray


array1 = [1, 2, 3, 4, 5]
array2 = [3, 2, 1]

print(indexProductExcepti(array1))
print(indexProductExcepti(array2))