  
    # PROBLEM 1:  
    #              Given a list of numbers a number k
    #              return whether any two numbers from the
    #              list add up
    #
    #              given [10, 15, 3, 7]
    #              and k of 17
    #              return true since 10 + 7 = 17
    # 

def findASum(array, sum):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] + array[j] == sum:
                return True
    return False

numbers = [ 10, 15, 3, 7 ]
k = 22

findASum(numbers, k)
