#!/usr/bin/env python3.8


def nb_year(p0, percent, aug, p):
    y_count = 0
    per = percent/100
    
    total_pop = p0
    
    while (total_pop <= p):
        total_pop = total_pop + (per*total_pop) + aug
        y_count = y_count + 1
        
    
    return y_count

print(nb_year(1500, 5, 100, 5000))