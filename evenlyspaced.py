#!/usr/bin/env python3.8

def evenlySpaced(a,b,c):
    numbers = [a,b,c]
    numbers = sorted(numbers)
    if (numbers[1] - numbers[0]) == (numbers[2] - numbers[1]):
        return True
    else:
        return False

print(evenlySpaced(2, 4, 6))
print(evenlySpaced(4, 6, 2)) 
print(evenlySpaced(4, 6, 3))
print(evenlySpaced(4, 60, 9))
       