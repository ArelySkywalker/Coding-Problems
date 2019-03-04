  
    # PROBLEM 1:  
    #              Given an array of integers, find the first 
    #              missing positive integer in linear time and constant space
    #              
    #              In other words, find the lowest positive integer that does
    #               not exist in the array
    #
    #              [3, 4, -1, 1] => return 1
    #              [1, 2, 0] => return 3
    # 
    # Author: Arely Miramontes Rodriguez
    #

def findAmissingPositiveInteger(array):
    if not array:
        return 1
    for i, num in enumerate(array):
        while i + 1 != array[i] and 0 < array[i] <= len(array):
            v = array[i]
            array[i], array[v - 1] = array[v - 1], array[i]
            array[v - 1] = v
            if array[i] == array[v - 1]:
                break
    for i, num in enumerate(array, 1):
        if num != i:
            return i
    return len(array) + 1


numbers = [ 3, 4, -1, 1 ]
numbers2 = [ 1, 2, 0 ]

print(findAmissingPositiveInteger(numbers))
print(findAmissingPositiveInteger(numbers2))
