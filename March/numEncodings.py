  
    # PROBLEM 1:  
    #              Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
    #              count the number of ways it can be decoded.
    #              For example, the message '111' would give 3, since it could be decoded 
    #              as 'aaa', 'ka', and 'ak'.
    #
    #              You can assume that the messages are decodable. 
    #              For example, '001' is not allowed.
    # 
    # Author: Arely Miramontes Rodriguez
    #

def numEncodings(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1: # This covers empty string
        return 1

    total = 0

    if int(s[:2]) <= 26:
        total += numEncodings(s[2:])

    total += numEncodings(s[1:])
    return total
