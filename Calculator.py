#!/usr/bin/env python3.8



x = float(input("Please enter your first number: "))
y = float(input("Please enter your second number: "))
print("This calculator can perform Addition(+), Subtraction(-), Multiplication(*) Division(/)")
op = input("Please enter the operation you would like to perform: ")


def calc(operator, n1, n2):
    
    switcher = {
        '+': lambda n1,n2: n1+n2,
        '-': lambda n1,n2: n1-n2,
        '*': lambda n1,n2: n1*n2,
        '/': lambda n1,n2: n1/n2
    }
    return switcher.get(operator)(n1,n2)

print("The result of" ,x, op, y, " is:" ,calc(op,x,y))


