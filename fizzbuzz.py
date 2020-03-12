#!/usr/bin/env python3.8

def three(arg1):
 x = ""
 y = ""
 z = " "
 if arg1 % 3 == 0:
    x = "Fizz"
 if arg1 % 5 == 0:
    y = "Buzz"
 else:
     z = "null"
 return x+y+z

print(three(30))
