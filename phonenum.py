#!/usr/bin/env python3.8

def create_phone_number(n):
    phone_beg ="".join(map(str,n[0:3]))
    phone_mid ="".join(map(str,n[3:6]))
    phone_end ="".join(map(str,n[6:]))
    phone_number = "(" + phone_beg + ") " + phone_mid + "-" + phone_end
    return phone_number


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) 