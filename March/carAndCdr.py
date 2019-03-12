  
    # PROBLEM 1:  
    #              cons(a, b) constructs a pair, and car(pair) and cdr(pair) 
    #              returns the first and last element of that pair.
    #              For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
    #
    #              Given this implementation of cons:
    #                def cons(a, b):
    #                   def pair(f):
    #                       return f(a, b)
    #                   return pair
    #
    #              Implement car and cdr.
    # 
    # Author: Arely Miramontes Rodriguez
    #

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def returnFirst(a,b):
        return a 
    return pair(returnFirst)

def cdr(pair):
    def returnLast(a,b):
        return b 
    return pair(returnLast)


print(car(cons(3,4)))
print(cdr(cons(3,4)))
