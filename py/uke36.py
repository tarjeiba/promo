#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:08:25 2019

@author: tarjei
"""

a = float( input(">>> a  = ") )
b = float( input(">>> b  = "))
c = float( input(">>> c  = "))
print(f"a = {a}, b = {b}, og c = {c}.")

# Vi ønsker å skrive ut "stort" dersom a > 10
# Vi ønsker å skrive ut "lite" dersom a <= 10
if a > 10:
    print("Stort")
else:
    print("Lite")