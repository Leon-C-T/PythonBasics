#!/usr/bin/env python3.8


def evendigits ():
    numlist = []
    for i in range (1000,3000):
        num = str(i)
        num = list(map(int, num))
        #print(num)
        if num[0] % 2 == 0 and num[1] % 2 == 0 and num[2] % 2 == 0 and num[3] % 2 == 0:
            numlist.append(i)
    
    return numlist
    

    
print(evendigits())