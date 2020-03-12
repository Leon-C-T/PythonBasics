#!/usr/bin/env python3.8

def largest(word):
    word =  word.split()
    word = list(map(int, word))
    print(word)
    x = [1]
    #x.append(sum(int(digit) for digit in str(word)))

    
    
    return max(x) 


print(largest("55 72 86")) 
print(largest("15 72 80 164")) 
print(largest("555 72 86 45 10"))