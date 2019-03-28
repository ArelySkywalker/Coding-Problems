# PROBLEM 1:  
    #               Run-length encoding is a fast and simple method of encoding strings. 
    #               The basic idea is to represent repeated successive characters as a 
    #               single count and character. For example, the string "AAAABBBCCDAA" 
    #               would be encoded as "4A3B2C1D2A".
    #
    #               Implement run-length encoding and decoding. You can assume the string 
    #               to be encoded have no digits and consists solely of alphabetic characters. 
    #               You can assume the string to be decoded is valid.
    #
    # 
    # Author: Arely Miramontes Rodriguez
    #

def runLengthEncodeDecode(st):

    # if the string contains no numbers, encode
    if st.isalpha():  

        encoded = ''
        while len(st) > 0:
            i = 0
            while i < len(st) and st[0] == st[i]:
                i += 1

            encoded += str(i) + st[0]
            st = st[i:]

        return encoded
    
    # decode since string contains numbers
    else:  

        return ''.join(c * int(n) for n, c in zip(st[::2], st[1::2]))
    
print(runLengthEncodeDecode('AAAABBBCCDAA'))
print(runLengthEncodeDecode('4A3B2C1D2A'))
