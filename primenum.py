#!/usr/bin/env python3.8

import sympy

def primenum (input1,input2):
    numlist = []
    for i in range(input1,input2):
        if sympy.isprime(i) == True:
            numlist.append(i)
    return numlist        

print(primenum(1000,3000))