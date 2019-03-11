  
    # PROBLEM 1:  
    #              Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
    #              Numbers can be 0 or negative.
    #              For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
    #              [5, 1, 1, 5] should return 10, since we pick 5 and 5.
    # 
    # Author: Arely Miramontes Rodriguez
    #

def largestSumOfAdjacent(integerList):
        for i in range(len(integerList)):
            for j in range(len(integerList)):
                if(i != j and array[i] + array[j] != array[i + 1]):
                    return array[i] + array[j]

myList = [2, 4, 6, 2, 5]
myList2 = [5, 1, 1, 5]
print(largestSumOfAdjacent(myList))
