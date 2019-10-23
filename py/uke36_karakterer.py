#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:53:32 2019

@author: tarjei
"""

p = input(">>> Hvor mange poeng? ")
p = float(p)
# Alternativ 1 
if p > 95:
    karakter = 6
else:
    if p > 80:
        karakter = 5
    else:
        if p > 60:
            karakter = 4
        else:
            if p > 40:
                karakter = 3
            else:
                if p > 25:
                    karakter = 2
                else:
                    karakter = 1
                    
if p > 95:
    karakter = 6
elif p > 80:
    karakter = 5
elif p > 60:
    karakter = 4
elif p > 40:
    karakter = 3
elif p > 25:
    karakter = 2
else:
    karakter = 1

print(f"Karaketeren din er {karakter}.")