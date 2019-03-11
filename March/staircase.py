
#   There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
#   Given N, write a function that returns the number of unique ways you can climb the staircase. 
#   The order of the steps matters.
#
#   For example, if N is 4, then there are 5 unique ways:
#   1, 1, 1, 1
#   2, 1, 1
#   1, 2, 1
#   1, 1, 2
#   2, 2
# 
# Author: Arely Miramontes Rodriguez
#

def staircase(n, X):
    S = [0 for _ in range(n + 1)]
    S[0] = 1
    for i in range(n + 1):
        S[i] += sum(S[i - x] for x in X if i - x > 0)
        S[i] += 1 if i in X else 0
    return S[-1]

steps = 4
rules = {1,2}

print(staircase(steps,rules))