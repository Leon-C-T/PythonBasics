#!/usr/bin/env python3.8

def triplestring(string):
    x = []
    for i in string:
       x.append(3*i)
    return "".join(x)

print(triplestring("tthwsrhhe"))
