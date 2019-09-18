#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dette programmet løser andregradslikningen 

a x ** 2 + b  + c = 0

og skriv er ut løsningene til brukeren.
@author: tarjei
"""
import math

# Ber brukeren om koeffisientene i likninga
a = float( input(">>> a = "))
b = float( input(">>> b = "))
c = float( input(">>> c = "))

# Regner ut diskriminanten
d = b ** 2 - 4 * a * c

if d > 0:
    print("Likninga har to løsninger.")
    print("--------------------------")
    # Regner ut ved å bruke abc-formelen
    x1 = (- b + math.sqrt(d)) / 2 * a
    x2 = (- b - math.sqrt(d)) / 2 * a
    print(f"Løsningene er {x1} og {x2}.")
elif d == 0:  # legg merke til dobbelt likhetstegn
    print("Likninga har én løsning.")
    print("------------------------")
    x = - b / (2 * a)
    print(f"Løsninga er i {x}.")
else:
    print("Likninga har ingen løsninger.")
