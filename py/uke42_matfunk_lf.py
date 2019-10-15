"""Dette programmet skriver ut en enkel funksjonstabell
for den matematiske funksjonen
f(x) = 3 * x ** 2 * lg(x) - 15

Laget av Tarjei
"""

import math

def f(x):
    return 3 * x ** 2 * math.log10(x) - 15

x = 20
print("   x     --     f(x)   ")
print("-----------------------")
while x <= 29:
    f_av_x = f(x)
    print(f"{x}    --    {f_av_x:.1f}")
    x += 1
