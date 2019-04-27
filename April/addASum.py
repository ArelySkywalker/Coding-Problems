#  
#   Given a list of numbers and a number k, 
#   return whether any two numbers from the list add up to k.
#
#   Example:
#   given [10, 15, 3, 7]
#   k = 17
#   return true since 10 + 7 = 17
# 
# Author: Arely Miramontes Rodriguez
#

def findAsum(arr,k):
    left = 0
    right = len(arr) - 1
    while(left < right):
        sum = arr[left] + arr[right]
        if(sum == k):
            return arr[left], arr[right]
        elif(sum > k):
            right = right - 1
        else:
            left = left + 1

numbers = [12, 15, 3, 2, 7]
k = 17
print(findAsum(numbers, k))